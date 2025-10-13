import json
import os
from pathlib import Path
from collections import defaultdict

# Define the plugin directories to analyze
plugins = ["EriData", "EriMap", "EriObject", "Jar API", "SkyzersPlugin", "StringIndex"]
base_path = Path(r"D:\pluginbuilder_release_2.0\plugins")

results = {}

for plugin in plugins:
    plugin_path = base_path / plugin
    plugin_results = {
        "procedures": [],
        "variables": []
    }

    # Check procedures
    procedures_path = plugin_path / "procedures"
    if procedures_path.exists():
        for json_file in procedures_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                versions = data.get("versions", [])
                has_1_21_1 = "1.21.1_NeoForge" in versions
                has_1_21_4 = "1.21.4_NeoForge" in versions

                if has_1_21_1 and not has_1_21_4:
                    # Check for corresponding code file
                    code_file_path = procedures_path / "code" / f"{json_file.stem}1.21.1NeoForge.txt"
                    has_code_file = code_file_path.exists()

                    plugin_results["procedures"].append({
                        "name": json_file.stem,
                        "path": str(json_file),
                        "has_code_file": has_code_file,
                        "versions": versions
                    })
            except Exception as e:
                print(f"Error reading {json_file}: {e}")

    # Check variables
    variables_path = plugin_path / "variables"
    if variables_path.exists():
        for json_file in variables_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                versions = data.get("versions", [])
                has_1_21_1 = "1.21.1_NeoForge" in versions
                has_1_21_4 = "1.21.4_NeoForge" in versions

                if has_1_21_1 and not has_1_21_4:
                    # Check for corresponding code file
                    code_file_path = variables_path / "code" / f"{json_file.stem}1.21.1NeoForge.txt"
                    has_code_file = code_file_path.exists()

                    plugin_results["variables"].append({
                        "name": json_file.stem,
                        "path": str(json_file),
                        "has_code_file": has_code_file,
                        "versions": versions
                    })
            except Exception as e:
                print(f"Error reading {json_file}: {e}")

    results[plugin] = plugin_results

# Print results
print("=" * 80)
print("NeoForge 1.21.4 Support - Inventory Report")
print("=" * 80)
print()

total_procedures = 0
total_variables = 0

for plugin, data in results.items():
    procedures = data["procedures"]
    variables = data["variables"]

    if procedures or variables:
        print(f"\n{'=' * 80}")
        print(f"PLUGIN: {plugin}")
        print(f"{'=' * 80}")

        if procedures:
            print(f"\nPROCEDURES TO UPDATE ({len(procedures)}):")
            print("-" * 80)
            for proc in procedures:
                print(f"  - {proc['name']}")
                print(f"    Path: {proc['path']}")
                print(f"    Has 1.21.1 Code File: {'YES' if proc['has_code_file'] else 'NO'}")
                print(f"    Current Versions: {', '.join(proc['versions'])}")
                print()
            total_procedures += len(procedures)

        if variables:
            print(f"\nVARIABLES TO UPDATE ({len(variables)}):")
            print("-" * 80)
            for var in variables:
                print(f"  - {var['name']}")
                print(f"    Path: {var['path']}")
                print(f"    Has 1.21.1 Code File: {'YES' if var['has_code_file'] else 'NO'}")
                print(f"    Current Versions: {', '.join(var['versions'])}")
                print()
            total_variables += len(variables)

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total Procedures to Update: {total_procedures}")
print(f"Total Variables to Update: {total_variables}")
print(f"Total Files to Update: {total_procedures + total_variables}")
print("=" * 80)
