FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Evita que python escriba archivos .pyc en el sistema

RUN apt-get update \
  # Dependencias para los paquetes de Python
  && apt-get install -y build-essential \
  # Dependencias de psycopg2
  && apt-get install -y libpq-dev \
  # Dependencias de traduccion
  && apt-get install -y gettext \
  # Dependencias de postgres
  && apt-get install -y postgresql \
  # Dependencias de locale
  && apt-get install -y locales locales-all\
  # Elimina archivos innecesarios
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ADD ./switch_web/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./switch_web /switch_web

# Copiamos el script de inicialización
COPY ./compose/dev/django/start-django ./start
RUN chmod +x start

WORKDIR /switch_web