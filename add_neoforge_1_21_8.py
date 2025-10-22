import json
import os
import shutil
from pathlib import Path

def process_procedure_json(json_path):
    """Process a procedure JSON file to add 1.21.8_NeoForge support"""
    print(f"\nProcessing procedure: {json_path}")

    # Read the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check if versions array exists
    if 'versions' not in data:
        print(f"  WARNING: No 'versions' array found in {json_path}")
        return

    # Check if 1.21.8_NeoForge is already in versions
    if '1.21.8_NeoForge' in data['versions']:
        print(f"  SKIP: 1.21.8_NeoForge already exists")
        return

    # Add 1.21.8_NeoForge to versions
    data['versions'].append('1.21.8_NeoForge')
    print(f"  ADDED: 1.21.8_NeoForge to versions array")

    # Save the updated JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    # Handle code files
    json_dir = os.path.dirname(json_path)
    json_name = os.path.splitext(os.path.basename(json_path))[0]

    # Check both in the same directory and in a 'code' subdirectory
    code_dirs = [
        json_dir,
        os.path.join(json_dir, 'code')
    ]

    for code_dir in code_dirs:
        if not os.path.exists(code_dir):
            continue

        target_code_file = os.path.join(code_dir, f"{json_name}1.21.8NeoForge.txt")

        # Check if code file already exists
        if os.path.exists(target_code_file):
            print(f"  SKIP: Code file {json_name}1.21.8NeoForge.txt already exists")
            return

        # Try to find source code file in order of preference
        source_candidates = [
            f"{json_name}1.21.4NeoForge.txt",
            f"{json_name}1.21.1NeoForge.txt",
            f"{json_name}1.20.4NeoForge.txt"
        ]

        source_file = None
        for candidate in source_candidates:
            candidate_path = os.path.join(code_dir, candidate)
            if os.path.exists(candidate_path):
                source_file = candidate_path
                print(f"  COPY: {candidate} -> {json_name}1.21.8NeoForge.txt")
                shutil.copy2(source_file, target_code_file)
                return

    # No code files found in any directory
    # This is normal for procedures without separate code files

def process_variable_json(json_path):
    """Process a variable JSON file to add 1.21.8_NeoForge support"""
    print(f"\nProcessing variable: {json_path}")

    # Read the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check if versions object exists
    if 'versions' not in data:
        print(f"  WARNING: No 'versions' object found in {json_path}")
        return

    # Check if 1.21.8_NeoForge key already exists
    if '1.21.8_NeoForge' in data['versions']:
        print(f"  SKIP: 1.21.8_NeoForge already exists")
        return

    # Try to find a source version to copy from (prefer 1.21.4_NeoForge, then 1.21.1_NeoForge)
    source_key = None
    for candidate in ['1.21.4_NeoForge', '1.21.1_NeoForge', '1.20.4_NeoForge']:
        if candidate in data['versions']:
            source_key = candidate
            break

    if not source_key:
        print(f"  WARNING: No source version found to copy from")
        return

    # Copy the version structure
    data['versions']['1.21.8_NeoForge'] = data['versions'][source_key].copy()
    print(f"  ADDED: 1.21.8_NeoForge key (copied from {source_key})")

    # Save the updated JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def process_plugin(plugin_path):
    """Process all procedures and variables in a plugin"""
    plugin_name = os.path.basename(plugin_path)
    print(f"\n{'='*60}")
    print(f"Processing plugin: {plugin_name}")
    print(f"{'='*60}")

    # Process procedures
    procedures_dir = os.path.join(plugin_path, 'procedures')
    if os.path.exists(procedures_dir):
        procedure_files = [f for f in os.listdir(procedures_dir) if f.endswith('.json')]
        print(f"\nFound {len(procedure_files)} procedure files")
        for proc_file in sorted(procedure_files):
            process_procedure_json(os.path.join(procedures_dir, proc_file))

    # Process variables
    variables_dir = os.path.join(plugin_path, 'variables')
    if os.path.exists(variables_dir):
        variable_files = [f for f in os.listdir(variables_dir) if f.endswith('.json')]
        print(f"\nFound {len(variable_files)} variable files")
        for var_file in sorted(variable_files):
            process_variable_json(os.path.join(variables_dir, var_file))

def main():
    base_dir = r"D:\pluginbuilder_release_2.0\plugins"

    plugins = [
        'EriMap',
        'StringIndex',
        'EriData',
        'EriObject',
        'SkyzersPlugin'
    ]

    for plugin_name in plugins:
        plugin_path = os.path.join(base_dir, plugin_name)
        if os.path.exists(plugin_path):
            process_plugin(plugin_path)
        else:
            print(f"\nWARNING: Plugin directory not found: {plugin_path}")

    print(f"\n{'='*60}")
    print("COMPLETE: All plugins processed")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
