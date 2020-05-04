#!/usr/bin/env bash

cd /ms104_market/ || exit 1
python manage.py migrate
python manage.py collectstatic --noinput
daphne -b 0.0.0.0 -p 8086 --access-log /var/log/ms104_market/daphne_access.log marketplace.asgi:application