#!/bin/sh

cd /app
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8080

#/usr/local/bin/gunicorn inventory.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app

