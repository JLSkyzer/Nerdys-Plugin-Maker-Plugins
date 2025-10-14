import json
import os
from pathlib import Path

def process_procedure_json(json_path):
    """Process a procedure JSON file to replace/remove 1.21.4_NeoForge versions."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        modified = False

        # Check if versions array exists and contains 1.21.4_NeoForge
        if 'versions' in data and isinstance(data['versions'], list):
            if '1.21.4_NeoForge' in data['versions']:
                if '1.21.1_NeoForge' in data['versions']:
                    # Remove 1.21.4_NeoForge if 1.21.1_NeoForge already exists
                    data['versions'].remove('1.21.4_NeoForge')
                    print(f"  Removed 1.21.4_NeoForge from {json_path.name}")
                else:
                    # Replace 1.21.4_NeoForge with 1.21.1_NeoForge
                    idx = data['versions'].index('1.21.4_NeoForge')
                    data['versions'][idx] = '1.21.1_NeoForge'
                    print(f"  Replaced 1.21.4_NeoForge with 1.21.1_NeoForge in {json_path.name}")
                modified = True

        # Save if modified
        if modified:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

        return modified
    except Exception as e:
        print(f"  ERROR processing {json_path}: {e}")
        return False

def process_variable_json(json_path):
    """Process a variable JSON file to replace/remove 1.21.4_NeoForge version keys."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        modified = False

        # Check if versions object exists and contains 1.21.4_NeoForge key
        if 'versions' in data and isinstance(data['versions'], dict):
            if '1.21.4_NeoForge' in data['versions']:
                if '1.21.1_NeoForge' in data['versions']:
                    # Remove 1.21.4_NeoForge if 1.21.1_NeoForge already exists
                    del data['versions']['1.21.4_NeoForge']
                    print(f"  Removed 1.21.4_NeoForge key from {json_path.name}")
                else:
                    # Rename key from 1.21.4_NeoForge to 1.21.1_NeoForge
                    data['versions']['1.21.1_NeoForge'] = data['versions'].pop('1.21.4_NeoForge')
                    print(f"  Renamed 1.21.4_NeoForge to 1.21.1_NeoForge in {json_path.name}")
                modified = True

        # Save if modified
        if modified:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

        return modified
    except Exception as e:
        print(f"  ERROR processing {json_path}: {e}")
        return False

def process_code_files(code_dir):
    """Process code files in procedures/code/ directory."""
    if not code_dir.exists():
        return

    # Get all 1.21.4NeoForge.txt files
    for file_path in code_dir.glob('*1.21.4NeoForge.txt'):
        base_name = file_path.stem.replace('1.21.4NeoForge', '')
        new_name_121 = f"{base_name}1.21.1NeoForge.txt"
        new_path_121 = code_dir / new_name_121

        if new_path_121.exists():
            # If 1.21.1 version exists, delete the 1.21.4 version
            file_path.unlink()
            print(f"  Deleted {file_path.name} (1.21.1 version already exists)")
        else:
            # Rename 1.21.4 to 1.21.1
            file_path.rename(new_path_121)
            print(f"  Renamed {file_path.name} to {new_name_121}")

def process_plugin(plugin_path):
    """Process a single plugin directory."""
    plugin_name = plugin_path.name
    print(f"\nProcessing {plugin_name}...")

    # Process procedures
    procedures_dir = plugin_path / 'procedures'
    if procedures_dir.exists():
        print(f"  Processing procedures JSON files...")
        for json_file in procedures_dir.glob('*.json'):
            process_procedure_json(json_file)

        # Process code files
        code_dir = procedures_dir / 'code'
        if code_dir.exists():
            print(f"  Processing code files...")
            process_code_files(code_dir)

    # Process variables
    variables_dir = plugin_path / 'variables'
    if variables_dir.exists():
        print(f"  Processing variables JSON files...")
        for json_file in variables_dir.glob('*.json'):
            process_variable_json(json_file)

def main():
    # Base directory
    base_dir = Path(r'd:\pluginbuilder_release_2.0\plugins')

    # List of plugins to process (excluding Jar API)
    plugins = ['EriData', 'EriMap', 'EriObject', 'StringIndex', 'SkyzersPlugin']

    print("Starting NeoForge version migration (1.21.4 -> 1.21.1)")
    print("=" * 60)

    for plugin_name in plugins:
        plugin_path = base_dir / plugin_name
        if plugin_path.exists():
            process_plugin(plugin_path)
        else:
            print(f"\nWARNING: Plugin directory not found: {plugin_name}")

    print("\n" + "=" * 60)
    print("Migration complete!")

if __name__ == '__main__':
    main()
