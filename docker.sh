#!/bin/bash
# -*- ENCODING: UTF-8 -*-

# Cargar las variables desde el archivo
source variables.txt

# Usar cut para obtener las primeras tres letras
codProyecto=$(echo "$proyecto" | cut -c1-3)

# Ahora puedes usar las variables en tu script
echo "Nombre del proyecto: $proyecto"
echo "Dominio: $dominio"
echo "Puerto: $puerto"
echo "Codigodel proyecto: $codProyecto"


cat > docker-compose.yml <<EOF
version: "3.9"

services:

  $codProyecto-dj:
    container_name: $codProyecto-dj
    build: .
    restart: always
    ports:
    - $puerto:8000
    volumes:
    - ./:/app
    depends_on:
      - $codProyecto-db

  $codProyecto-db:
    image: postgres:14.3-alpine3.16
    container_name: $codProyecto-db
    ports:
      - 5431:5432
    environment:
      - POSTGRES_DB=$proyecto
      - POSTGRES_USER=magoreal
      - POSTGRES_PASSWORD=ojalaque
    volumes:
      - ./db:/var/lib/postgresql/data
EOF

cat > Dockerfile <<EOF

FROM python:3.10.4-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements/base.txt ./
COPY requirements/prod.txt ./

RUN pip install -r prod.txt

COPY ./ ./

CMD ["sh", "entrypoint.sh"]
EOF

cat > entrypoint.sh <<EOF

echo 'Running collectstatic...'
python manage.py collectstatic --noinput --settings=settings.prod

echo 'Running migrations...'
python manage.py migrate --settings=settings.prod

echo 'Runing Server...'
gunicorn config.wsgi:application DJANGO_SETTINGS_MODULE=settings.prod --bind 0.0.0.0:8000
EOF