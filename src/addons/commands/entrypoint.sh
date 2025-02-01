#!/bin/bash
set -e  # Завершувати скрипт при помилках

python src/manage.py makemigrations --noinput
python src/manage.py migrate

python src/manage.py runserver 0.0.0.0:8000

