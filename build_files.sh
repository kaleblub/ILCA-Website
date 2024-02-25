#!/bin/bash

echo "--Creating virtual environment--"
python3 -m venv venv
echo "--Activating virtual environment--"
source venv/bin/activate
echo "--Installing requirements--"
pip install -r requirements/production.txt
echo "--Upgrading pip and installing psycopg2-binary--"
/vercel/path0/venv/python3 -m pip install --upgrade pip
pip install psycopg2-binary

echo "--Collecting Static Files--"
python3 manage.py collectstatic --noinput

# Set PYTHONPATH to the project root directory
export PYTHONPATH="/vercel/path0/$(basename "$(pwd)")"
