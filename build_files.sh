#!/bin/bash

echo "Installing pip Packages"
/vercel/path0/venv/python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/production.txt
pip install psycopg2-binary

echo "Collecting Static Files"
python3 manage.py collectstatic --noinput

# Set PYTHONPATH to the project root directory
export PYTHONPATH="/vercel/path0/$(basename "$(pwd)")"
