import os
import ast
import requests
import json

severity_mapping = {
    "AL": "Warning",
    "AM": "Error",
    "CP": "Info",
    "LT":  "Info",
    "CV": "Info",
    "JJ":  "Warning",
    "RF": "Error",
    "ST": "Error",
    "TQ": "Warning",
}

category_mapping = {
    "AL": "CodeStyle",       
    "AM": "ErrorProne",      
    "CP": "CodeStyle",      
    "LT": "CodeStyle",       
    "CV": "BestPractice",    
    "JJ": "Compatibility",  
    "RF": "ErrorProne",      
    "ST": "ErrorProne",      
    "TQ": "CodeStyle",       
}

enabled_rules = [
        "ST01",
        "ST03",
        "ST06",
        "ST07",
        "RF01",
        "RF02",
        "LT01",
        "LT02",
        "LT04",
        "CP01",
        "CP02",
        "AL01",
        "AL02",
        "AM01"
        ]

def downloadRules():
    API_URL = "https://api.github.com/repos/sqlfluff/sqlfluff/git/trees/main?recursive=1"
    response = requests.get(API_URL,timeout=10)
    response.raise_for_status()
    tree = response.json().get("tree", [])

    for item in tree:
        path = item["path"]
        if path.startswith("src/sqlfluff/rules/") and path.endswith(".py"):
            print("Downloading", path)
            raw_url = f"https://raw.githubusercontent.com/sqlfluff/sqlfluff/main/{path}"
            r = requests.get(raw_url,timeout=10)
            r.raise_for_status()
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(r.content)

def extractRules():
    rules = []
    for root, _, files in os.walk("src/sqlfluff/rules"):
        for fname in files:
            if not fname.endswith(".py"):
                continue

            path = os.path.join(root, fname)
            with open(path, encoding="utf8") as f:
                tree = ast.parse(f.read(), path)

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name.startswith("Rule_"):
                    bases = [b.id if isinstance(b, ast.Name) else b.attr for b in node.bases]
                    if any(x in bases for x in ["BaseRule", "Rule_AL04", "Rule_AL01", "Rule_LT03", "Rule_CP01"]):
                        rule_id = node.name.split("_", 1)[1]
                        doc = ast.get_docstring(node) or ""

                        # Extract 'name' attribute from the class body
                        rule_name = None
                        for stmt in node.body:
                            if isinstance(stmt, ast.Assign):
                                for target in stmt.targets:
                                    if isinstance(target, ast.Name) and target.id == "name":
                                        if isinstance(stmt.value, ast.Constant):  # Python 3.8+
                                            rule_name = stmt.value.value
                                        elif isinstance(stmt.value, ast.Str):    # Older Python versions
                                            rule_name = stmt.value.s
                                        break
                            if rule_name:
                                break

                        full_id = f"{rule_id}_{rule_name}"
                        rules.append((rule_id, full_id, doc))
    return rules


def get_brief_description(doc):
    if not doc:
        return "NoDescription"
    first = doc.strip().splitlines()[0].rstrip(".")
    words = first.split()
    return "_".join(words[:5]).capitalize()

def createDescriptions(rules):
    out_dir = "docs/description"
    os.makedirs(out_dir, exist_ok=True)

    # 1) Write all current descriptions
    for _, full_id, doc in rules:
        with open(f"{out_dir}/{full_id}.md", "w", encoding="utf8") as f:
            f.write(f"# {full_id}\n\n{doc.strip()}\n")

    # 2) Prune stale files
    keep = {f"{full_id}.md" for _, full_id, _ in rules}
    for fname in os.listdir(out_dir):
        if fname.endswith(".md") and fname not in keep:
            print(f"Removing stale description: {fname}")
            os.remove(os.path.join(out_dir, fname))

def buildPatterns(rules):
    patterns = []
    for rule_id, full_id, _ in rules:
        prefix = rule_id[:2]
        level = severity_mapping.get(prefix, "Info")
        category = category_mapping.get(prefix, "Other")
        patterns.append({
            "patternId": full_id,
            "level": level,
            "category": category,
            "parameters": [],
            "enabled": rule_id[:4] in enabled_rules
        })

    data = {
        "name": "sqlfluff",
        "version": get_sqlfluff_version(),
        "patterns": patterns
    }

    # Always overwrite
    with open("docs/patterns.json", "w", encoding="utf8") as f:
        json.dump(data, f, indent=2)
    
    return patterns

def get_sqlfluff_version():
    """Gets the version of the 'sqlfluff' package from the requirements.txt file."""
    try:
        with open("requirements.txt", 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('sqlfluff'):
                    # Split the line at the first occurrence of '==' to get the version
                    package, version = line.split('==') if '==' in line else (line, None)
                    print(package, version)
                    return version.strip() if version else None
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def writeAllPatternsTests(patterns_data):
    # Path to the output XML file
    all_patterns_xml = os.path.join(os.getcwd(), "docs", "multiple-tests", "all-patterns", "patterns.xml")
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(all_patterns_xml), exist_ok=True)

    with open(all_patterns_xml, "w", encoding="utf-8") as xml_file:
        # Start the root module
        xml_file.write('<module name="root">\n')
        # Write the BeforeExecutionExclusionFileFilter module with property
        xml_file.write('    <module name="BeforeExecutionExclusionFileFilter">\n')
        xml_file.write('        <property name="fileNamePattern" value=".*\\.json" />\n')
        xml_file.write('    </module>\n')
        
        # Write each pattern module on a new line with proper indentation
        for pattern in patterns_data:
            xml_file.write(f'    <module name="{pattern["patternId"]}" />\n')
        # Close the root module
        xml_file.write('</module>\n')
        
def writeDescriptionJson(rules):
    output = []
    for rule_id, full_id, doc in rules:
        title = get_brief_description(doc).replace("_", " ")
        entry = {
            "patternId": full_id,
            "title": title,
            "description": doc.strip(),
            "timeToFix": 5,
            "parameters": []
        }
        output.append(entry)

    out_path = os.path.join("docs", "description", "description.json")
    with open(out_path, "w", encoding="utf8") as f:
        json.dump(output, f, indent=2)
    print(f"✅ Wrote {len(output)} entries to {out_path}")


def main():
    downloadRules()
    rules = extractRules()
    createDescriptions(rules)
    patterns = buildPatterns(rules)
    writeAllPatternsTests(patterns)
    writeDescriptionJson(rules)
    print("✅ descriptions, patterns.json and description.json generated!")


if __name__ == "__main__":
    main()