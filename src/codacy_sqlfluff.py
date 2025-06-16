import os
import sys
import json
import jsonpickle
from subprocess import Popen, PIPE
import glob
import signal
from contextlib import contextmanager
import traceback


@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, lambda: sys.exit(2))
    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)
    yield


DEFAULT_TIMEOUT = 15 * 60


def getTimeout(timeoutString):
    if not timeoutString.isdigit():
        return DEFAULT_TIMEOUT
    return int(timeoutString)


class Result:
    # result need be formatted as JSON
    # expected = '{"filename": "file.py",
    #              "message": "message",
    #              "patternId": "id", "line": 80}'
    def __init__(self, filename, message, patternId, line):
        self.filename = filename
        self.message = message
        self.patternId = patternId
        self.line = line

    def __str__(self):
        return f"Result({self.filename},{self.message},{self.patternId},{self.line})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        return (
            self.filename == o.filename,
            self.message == o.message,
            self.patternId == o.patternId,
            self.line == o.line,
        )


def toJson(obj):
    return jsonpickle.encode(obj, unpicklable=False)


def readJsonFile(path):
    with open(path, "r", encoding="utf-8") as file:
        res = json.loads(file.read())
    return res

def run_sqlfluff(options, files, cwd=None):
 
    process = Popen(
        ["sqlfluff", "lint", "--format", "json"],
        stdout=PIPE,
        cwd=cwd
    )
    stdout = process.communicate()[0]
    result = stdout.decode("utf-8")

    return result


def chunks(lst, n):
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def run_sqlfluff_results(options, files, cwd):
    results = []
    res = run_sqlfluff(options, files, cwd)
    sqlfluff_dicts = json.loads(res)

    ### Example of a result
    #
    # "filepath": "test.sql",
    # "violations": [
    #     {
    #     "start_line_no": 1,
    #     "start_line_pos": 1,
    #     "code": "LT09",
    #     "description": "Select targets should be on a new line unless there is only one select target.",
    #     "name": "layout.select_targets",
    #     "warning": False,
    #     "fixes": [],
    #     "start_file_pos": 0,
    #     "end_line_no": 2,
    #     "end_line_pos": 9,
    #     "end_file_pos": 28
    # }
    # ]

    for res in sqlfluff_dicts:
        for issue in res['violations']:
            filename = res["filepath"]
            message = f"{issue['description']} ({issue['code']})"
            patternId = f"{issue['code']}_{issue['name']}"
            line = issue["start_line_no"]
            results.append(Result(filename, message, patternId, line))
    return results


def walkDirectory(directory):
    def generate():
        for filename in glob.iglob(os.path.join(directory, "**/*.sql"), recursive=True):
            res = os.path.relpath(filename, directory)
            yield res

    return list(generate())

def readConfiguration(configFile, srcDir):
    def allFiles(): 
        return walkDirectory(srcDir)

    try:
        configuration = readJsonFile(configFile)
        files = configuration.get('files') or allFiles()
        tools = [t for t in configuration['tools'] if t['name'] == 'sqlfluff']

        if tools and 'patterns' in tools[0]:
            sqlfluff = tools[0]
            tools = [p["patternId"].split("_")[0] for p in sqlfluff.get("patterns") or []]
            ## all patterns have a code and only that code is needed to run --rules flag
            listPatterns = ",".join(tools)
            options = ["--dialect", "postgres", "--rules", listPatterns]
        else:
            options = []
    except Exception:
        files = allFiles()
        options = []

    print(options)
    return (options, [f for f in files])

def run_tool(configFile, srcDir):
    (options, files) = readConfiguration(configFile, srcDir)
    res = []
    filesWithPath = [os.path.join(f) for f in files]

    for chunk in chunks(filesWithPath, 10):
        res.extend(run_sqlfluff_results(options, chunk, srcDir))

    for result in res:
        if result.filename.startswith(srcDir):
            result.filename = os.path.relpath(result.filename, srcDir)
    
    return res

def results_to_json(results):
    return os.linesep.join([toJson(res) for res in results])

if __name__ == "__main__":
    with timeout(getTimeout(os.environ.get("TIMEOUT_SECONDS") or "")):
        try:
            results = run_tool("/.codacyrc", "/src")
            results = results_to_json(results)
            print(results)
        except Exception:
            traceback.print_exc()
            sys.exit(1)

