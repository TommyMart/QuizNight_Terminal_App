#!/bin/bash


# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed. Please ensure version below is higher than 3.8."

    # Print to terminal what version is installed
    python3 --version
    
    # Advise if version is less than to please install
    echo "If your version is less than 3.8, please download the latest version from the Official Python website. Link to site in readme.md."

# If Python 3 is not installed, asked user to please install and try again
else
    echo "Python 3 is not installed. Please install Python 3.8 or above and try again."

fi