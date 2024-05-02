#!/bin/bash

# Make sure python3check.sh is executable 
chmod +x scripts/python3check.sh

# Checks if Python 3 is installed
scripts/python3check.sh || { echo "Failed to check for Python 3."; exit 1; }

# Create virtual environment 
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate || { echo "Failed to activate virtual environment."; exit 1; }

# Make sure dependencies.sh is executable
chmod +x scripts/dependencies.sh

# Run dependencies.sh script
scripts/dependencies.sh || { echo "Failed to install dependencies."; exit 1; }
# pip3 install rich

# Finally run main.py to start the app
python3 main.py 