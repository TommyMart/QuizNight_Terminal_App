#!/bin/bash

# This package has already been installed and ran
# on the code in the py python files

# It was ran by executing: chmod +x scripts/autopep8.sh
# Then running: scripts/autopep8.sh

# Install AutoPep 8
python3 -m pip install autopep8

# Run autopep8 with in-place and double aggressive
autopep8 --in-place -a -a main.py
autopep8 --in-place -a -a quiz_functions.py
autopep8 --in-place -a -a quizzes.py
