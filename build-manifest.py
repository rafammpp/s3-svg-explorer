# a python script tha builds a json representation for the current directory and all subdirectories
# the json contains the dir names an it's files. Every dir is a key and it's value is a list of files.
# the file paths should be relative to the initial directory (the one that is passed as an argument)
# the json is like this:
# { 
#   "dir1": ["file1", "file2", ...],
#   "dir2": ["file1", "file2", ...],
# outputs the json to manifest.json
# usage: python build-manifest.py [dir_path]

import os
import sys
import json


def get_file_name(file_path):
    return os.path.basename(file_path)

def get_relative_file_path(file_path):
    return file_path.removeprefix(dir_path).removeprefix('/')

def main():
    manifest = {}
    for root, dirs, files in os.walk(dir_path):
        root_path = get_relative_file_path(root)
        # sort files alphabetically
        files.sort()
        manifest[root_path] = [root_path + '/' + file for file in files if file.endswith('.svg')]
        if not manifest[root_path]:
            del manifest[root_path]
    
    # sort keys alphabetically
    manifest = dict(sorted(manifest.items()))

    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=4)
    
# get from arg the target directory
# if arg is not provided, use the current directory

dir_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
dir_path = os.path.abspath(dir_path)

if not os.path.isdir(dir_path):
    raise Exception("Invalid directory path")
os.chdir(dir_path)

# remove manifest.json if exists
if os.path.exists("manifest.json"):
    os.remove("manifest.json")

if __name__ == "__main__":
    main()