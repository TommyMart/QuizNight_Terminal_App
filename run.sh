#!/bin/bash

python -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
# pip3 install rich
python3 main.py