import json
import os
import argparse

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Define the placeholders and their replacements with unique markers
placeholders = {
    "${{ values.namespace }}": f"__PLACEHOLDER_NAMESPACE__{config['namespace']}__",
    "${{ values.name }}": f"__PLACEHOLDER_NAME__{config['name']}__"
}

# Function to replace placeholders in a file
def replace_in_file(file_path, reverse=False):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Skipping non-UTF-8 file: {file_path}")
        return

    for placeholder, value in placeholders.items():
        if reverse:
            content = content.replace(value, placeholder)
        else:
            content = content.replace(placeholder, value)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to process files and directories
def process_directory(directory, reverse=False):
    for root, dirs, files in os.walk(directory, topdown=False):
        # Skip .idea directory
        dirs[:] = [d for d in dirs if d != '.idea']
        
        # Process files
        for file_name in files:
            file_path = os.path.join(root, file_name)
            replace_in_file(file_path, reverse)
            new_name = file_name
            for placeholder, value in placeholders.items():
                if reverse:
                    new_name = new_name.replace(value, placeholder)
                else:
                    new_name = new_name.replace(placeholder, value)
            if new_name != file_name:
                os.rename(file_path, os.path.join(root, new_name))
        
        # Process directories
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            new_name = dir_name
            for placeholder, value in placeholders.items():
                if reverse:
                    new_name = new_name.replace(value, placeholder)
                else:
                    new_name = new_name.replace(placeholder, value)
            if new_name != dir_name:
                try:
                    os.rename(dir_path, os.path.join(root, new_name))
                except OSError as e:
                    print(f"Skipping non-empty directory: {dir_path}")

# Argument parsing
parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('directory', type=str, help='Directory to process')
parser.add_argument('--reverse', action='store_true', help='Reverse the replacement')
args = parser.parse_args()

# Process the directory
process_directory(args.directory, args.reverse)