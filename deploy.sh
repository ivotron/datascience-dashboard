#!/bin/bash
#
# To deploy on a remote machine via ssh, set a value for DOCKER_HOST:
#
#   export DOCKER_HOST="ssh://myuser@hostname"
#
# the above assumes:
#
#  1. `myuser` has passwordless access to `hostname`
#  2. the `myuser` account can run docker on the remote machine
#
set -e

# rebuild
docker-compose -f docker/docker-compose.yml build

# restart
docker-compose -f docker/docker-compose.yml up --detach

# this is idempotent: if admin user exists, it's not recreated and
# command doesn't exit with non-zero code.
docker exec mldashes flask fab create-admin \
  --username admin \
  --firstname admin \
  --lastname admin \
  --email admin@admin.com \
  --password admin
