#!/bin/sh

set -e

python manage.py wait_for_db

python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module config.wsgi --py-autoreload 3
