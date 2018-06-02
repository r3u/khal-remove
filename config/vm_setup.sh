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
sudo apt-get -y install sox
sudo apt-get -y install libsox-fmt-all
sudo apt-get -y install python3-pip
sudo apt-get -y install python3-flask
sudo apt-get -y install python3-psycopg2
sudo apt-get -y install python3-redis
sudo apt-get -y install python3-celery
sudo apt-get -y install python3-sqlalchemy

sudo pip3 install sox

sudo groupadd khal-service
sudo usermod -a -G khal-service celery
sudo usermod -a -G khal-service vagrant
sudo mkdir -p /var/lib/khal-remove/{uploads,results,temp}
sudo chown -R vagrant:khal-service /var/lib/khal-remove
sudo chmod g+w /var/lib/khal-remove/results
sudo chmod g+wx /var/lib/khal-remove/temp

sudo cp /workspace/config/celeryd /etc/default/celeryd
sudo ln -s /workspace/config/khal-remove.service /lib/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable khal-remove

sudo systemctl restart celeryd
sudo systemctl restart khal-remove
