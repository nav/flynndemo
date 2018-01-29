#!/bin/bash

export DJANGO_SETTINGS_MODULE=inventory.settings
export DJANGO_SECRET_KEY=xxx

python manage.py collectstatic --noinput

current_dir=`pwd`

cd /tmp
tar czf static.tgz static
rm -rf static
mv static.tgz $current_dir
