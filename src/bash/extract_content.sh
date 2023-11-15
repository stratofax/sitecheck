#!/bin/bash

#######################################
# extract content from Cadent blog pages
#######################################

# turn on output for debugging
#set -x
# turn off output for production
set +x
# turn on unoffical bash strict mode
set -euo pipefail
#######################################

SC='/home/neil/Repos/stratofax/sitecheck/src/'
# Define the parent directory
PARENT_DIR="/home/neil/Repos/cadentcom/website-relaunch/converted/posts/"

# Loop through each subdirectory
for subdir in "$PARENT_DIR"/*; do
    # Check if it's a directory
    if [ -d "$subdir" ]; then
        echo "Extracting content from $subdir"

        # Enter the subdirectory
        cd "$subdir"

        # Place your commands here
        # Example: echo "This is a command running in $(pwd)"
        cat index.html | python3 $SC/sitecheck/get_cadent_meta.py
        cat index.html | python3 $SC/sitecheck/extract_div.py entry-content | python3 $SC/sitecheck/remove_element.py img noscript div > extracted.html
        # check for span tags
        cat extracted.html | python3 $SC/sitecheck/list_attribs.py span

        # Return to the parent directory
        cd "$PARENT_DIR"

    fi
done

echo "All content extraction complete."



