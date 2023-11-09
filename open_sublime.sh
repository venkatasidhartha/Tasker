#!/bin/bash

python3 appendDateinFile.py
file_path=$(jq '.file_path' config.json)
new_str=$(sed -e 's/"//g' <<< "$file_path")
subl $new_str
