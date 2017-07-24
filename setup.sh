#!/bin/bash
sudo apt-get update
sudo apt-get install python3.5 python3.5-dev python3.5-venv -y
python3.5 -m venv env
. env/bin/activate
pip install -r requiments.txt
