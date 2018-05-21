#!/bin/bash

set -eu

export DEBIAN_FRONTEND=noninteractive

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install vim
sudo apt-get -y install redis-server
sudo apt-get -y install celeryd
sudo apt-get -y install gunicorn3
sudo apt-get -y install ipython3
sudo apt-get -y install python3-flask
sudo apt-get -y install python3-psycopg2
sudo apt-get -y install python3-redis
sudo apt-get -y install python3-celery
sudo apt-get -y install python3-sqlalchemy

sudo cp /workspace/celeryd /etc/default/celeryd

sudo systemctl restart celeryd
