#!/bin/sh

echo 'Running collectstatic...'
python manage.py collectstatic --noinput --settings=settings.prod

echo 'Running migrations...'
python manage.py migrate --settings=settings.prod

echo 'Runing Server...'
gunicorn settings.wsgi:application DJANGO_SETTINGS_MODULE=settings.prod --bind 0.0.0.0:8000