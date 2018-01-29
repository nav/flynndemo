web: gunicorn -w 2 -b 0.0.0.0:$PORT inventory.wsgi --log-file -
worker: celery -A inventory worker --loglevel=info
