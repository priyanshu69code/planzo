#!/bin/sh

# Wait for PostgreSQL to be ready
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for PostgreSQL..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

pipenv shell

# Apply database migrations
python planzo/manage.py migrate

# Collect static files
python planzo/manage.py collectstatic --no-input

# Start Gunicorn
exec gunicorn --bind 0.0.0.0:8000 --chdir planzo config.wsgi:application
