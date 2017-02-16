#!/bin/bash

export DJANGO_SETTINGS_MODULE=inventory.local_settings

python manage.py collectstatic --noinput

tar czf static.tgz static

rm -rf static