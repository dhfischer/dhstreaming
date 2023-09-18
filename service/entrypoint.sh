#!/bin/sh

echo "Executing the container"

#
#  WAIT FOR DATABASE
#
echo "Waiting for postgres..."
echo "${POSTGRES_HOST}:5432"
while ! nc -z "$POSTGRES_HOST" 5432; do
  sleep 1
done
echo "PostgreSQL started"

#
#  APPLY DATABASE MIGRATIONS
#
python manage.py migrate

#
#  GENERATE INITIAL DATA FOR TESTING
#
#  This is just a helper code. It should be present only in the
#  first deploy to generate data for testing.
#
python populate.py

#
#  EXECUTE THE APPLICATION
#
gunicorn --bind :8000 --workers 3 service.wsgi:application

exec "$@"
