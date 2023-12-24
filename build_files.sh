#!/bin/bash

echo "Installing pip Packages"
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/production.txt

echo "Collecting Static Files"
# mkdir staticfiles
python3 manage.py collectstatic --noinput

# Set PYTHONPATH to the project root directory
export PYTHONPATH="/vercel/path0/$(basename "$(pwd)")"
