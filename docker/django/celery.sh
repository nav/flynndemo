#!/bin/sh

cd /app
/usr/local/bin/celery -A inventory worker --loglevel=info
