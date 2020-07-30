#!/bin/bash
set -eux

# add /app link pointing to workspace folder
rm -r /app
ln -s /workspace /app

# start meinheld-gunicorn-flask
/entrypoint.sh /start.sh &

# give it some time to start
sleep 10

# create user
flask fab create-admin \
  --username $ADMIN_USER \
  --firstname $ADMIN_FIRST \
  --lastname $ADMIN_LAST \
  --email $ADMIN_EMAIL \
  --password $ADMIN_PASS

# block and wait for server to stop
wait
