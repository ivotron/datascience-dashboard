FROM tiangolo/meinheld-gunicorn-flask:python3.8-2020-06-06

ENV NGINX_WORKER_PROCESSES auto

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY entrypoint.sh /dashboard_entrypoint.sh

ENTRYPOINT ["/dashboard_entrypoint.sh"]
