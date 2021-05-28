#! /bin/bash

python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt
python3 ./main.py&
