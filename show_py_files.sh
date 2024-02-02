#!/bin/bash

# Loop through each .py file in the current directory
for file in *.py; do
    echo "File: $file"
    echo "----------------"
    cat "$file"
    echo
    echo
done

