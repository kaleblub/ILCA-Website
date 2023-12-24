#!/bin/bash

echo "Installing pip Packages"
pip install --upgrade pip
pip install -r requirements/production.txt

echo "Collecting Static Files"
# mkdir staticfiles
python3 manage.py collectstatic --noinput