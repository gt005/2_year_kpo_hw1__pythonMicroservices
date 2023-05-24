FROM python:3.11

ENV PYTHONUNBUFFERED 1

COPY . /api_app

WORKDIR ./api_app

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY django_entrypoint.sh /django_entrypoint.sh
RUN chmod +x /django_entrypoint.sh

ENTRYPOINT ["/django_entrypoint.sh"]