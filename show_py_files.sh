#!/bin/bash

# Function to display file contents with timestamp
display_file_contents() {
    echo "File: $1"
    echo "Last Modified: $(date -r $1)"
    echo "----------------"
    cat "$1"
    echo
    echo
}

if [ "$1" == "--recent" ]; then
    # Display the most recently modified .py file
    recent_file=$(ls -t *.py | head -n 1)
    display_file_contents "$recent_file"
else
    # Loop through each .py file in the current directory
    for file in *.py; do
        display_file_contents "$file"
    done
fi
