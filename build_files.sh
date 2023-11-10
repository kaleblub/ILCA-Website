#!/bin/bash

echo "Installing pip Packages"
pip install -r requirements.txt

echo "Collecting Static Files"
# mkdir staticfiles
python manage.py collectstatic --noinput