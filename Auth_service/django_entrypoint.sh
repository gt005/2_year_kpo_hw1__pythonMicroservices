#!/bin/bash

# Ждем, пока PostgreSQL будет доступен для подключения
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "Waiting for PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT to become available..."
  sleep 2
done

python manage.py makemigrations
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000