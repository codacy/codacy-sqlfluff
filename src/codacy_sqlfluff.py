import os
import sys
import json
import jsonpickle
from subprocess import Popen, PIPE
import glob
import signal
from contextlib import contextmanager
import traceback
import tempfile


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
        ["sqlfluff", "lint", "--format", "json"] + options + files,
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
    
    # Check if the result is an empty string. If so, there are no violations.
    if not res:
        return []

    try:
        sqlfluff_dicts = json.loads(res)
        for res_dict in sqlfluff_dicts:
            # Ensure 'violations' key exists and is not empty
            if 'violations' in res_dict and res_dict['violations']:
                for issue in res_dict['violations']:
                    filename = res_dict["filepath"]
                    message = f"{issue['description']} ({issue['code']})"
                    patternId = f"{issue['code']}_{issue['name']}"
                    line = issue["start_line_no"]
                    results.append(Result(filename, message, patternId, line))
    except json.JSONDecodeError:
        # This prevents the program from crashing on malformed JSON.
        print(f"Error decoding JSON from sqlfluff output: {res}", file=sys.stderr)
        return []

    return results

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

def walkDirectory(directory):
    def generate():
        for filename in glob.iglob(os.path.join(directory, "**/*.sql"), recursive=True):
            res = os.path.relpath(filename, directory)
            yield res

    return list(generate())

def readConfiguration(configFile, srcDir):
    def allFiles(): 
        return walkDirectory(srcDir)

    options = []
    
    # Default sqlfluff configuration
    dialect = "postgres"
    skip_byte_limit_flag = 150000

    try:
        configuration = readJsonFile(configFile)
        files = configuration.get('files') or allFiles()
        tools = [t for t in configuration['tools'] if t['name'] == 'sqlfluff']

        if tools and 'patterns' in tools[0]:
            sqlfluff_tool = tools[0]
            patterns = [p["patternId"].split("_")[0] for p in sqlfluff_tool.get("patterns") or []]
            listPatterns = ",".join(patterns)

            # Generate a temporary sqlfluff config file
            tmp = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.sqlfluff')
            tmp.write("[sqlfluff]\n")
            tmp.write(f"dialect = {dialect}\n")
            tmp.write(f"large_file_skip_byte_limit = {skip_byte_limit_flag}\n")

            # Write rules or exclude all rules based on patterns on .codacyrc
            if listPatterns:
                tmp.write(f"rules = {listPatterns}\n")
            else:
                tmp.write("exclude_rules = all\n")
            tmp.close()

            # Add the generated config file to options
            options.extend(["--config", tmp.name])

    except Exception:
        files = allFiles()

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

