FROM python:3.6-slim-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir -p -m 1777 /tmp/media \
    && mkdir -p -m 1777 /tmp/static


# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django

COPY ./docker/django/django.sh /usr/local/bin/django.sh
COPY ./docker/django/celery.sh /usr/local/bin/celery.sh

RUN sed -i 's/\r//' /usr/local/bin/django.sh \
    && chmod +x /usr/local/bin/django.sh \
    && chown django /usr/local/bin/django.sh

RUN sed -i 's/\r//' /usr/local/bin/celery.sh \
    && chmod +x /usr/local/bin/celery.sh \
    && chown django /usr/local/bin/celery.sh

WORKDIR /app
