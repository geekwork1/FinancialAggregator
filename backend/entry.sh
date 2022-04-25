#!/usr/bin/env bash

echo 'Run backend'
sleep 3

python manage.py migrate
python manage.py runserver 0.0.0.0:7000 -insecure