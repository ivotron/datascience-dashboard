FROM tiangolo/meinheld-gunicorn-flask:python3.8-2020-06-06

ENV NGINX_WORKER_PROCESSES auto

COPY app/requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app
