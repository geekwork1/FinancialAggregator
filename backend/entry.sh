#!/bin/bash

>&1 echo "Postgres is started to entry.sh"



#until PGPASSWORD="FA@2022" psql -h "db" -d "finaggregator" -U "finaggregator" -c '\q'; do
until PGPASSWORD="${POSTGRES_PASSWORD}" psql -h "${POSTGRES_HOST}" -d "${POSTGRES_DB}" -U "${POSTGRES_USER}" -c '\q'; do
  >&2 echo "Postgres is unavaible - sleeping"
  sleep 1
done

>&1 echo "Postgres is up - executing command"

USER="${POSTGRES_USER}"

python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
#gunicorn backend.wsgi -b 0.0.0.0:8080


