#!/usr/bin/env bash

cd /ms104_market/ || exit 1
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn marketplace.wsgi:application --bind 0.0.0.0:8086 \
            --error-logfile /var/log/ms104_market/gunicorn_error.log \
            --access-logfile /var/log/ms104_market/gunicorn_access.log \
            --workers 2
