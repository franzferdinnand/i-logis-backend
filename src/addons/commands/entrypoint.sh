#!/bin/bash
set -e  # Завершувати скрипт при помилках

/app/src/addons/commands/wait-for-it.sh postgres:5432 --timeout 10

python src/manage.py makemigrations --noinput
python src/manage.py migrate

python src/manage.py runserver 0.0.0.0:8000

