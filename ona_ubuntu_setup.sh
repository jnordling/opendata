#!/bin/bash
# SetUp Script For

echo "----- Starting Instalations -------"

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y default-jre 
sudo apt-get install -y gcc 
sudo apt-get install -y git 
sudo apt-get install -y python-dev 
sudo apt-get install -y python-virtualenv 
sudo apt-get install -y libjpeg-dev 
sudo apt-get install -y libfreetype6-dev 
sudo apt-get install -y zlib1g-dev 
sudo apt-get install -y rabbitmq-server 
sudo apt-get install -y build-essential 
sudo apt-get install -y libxslt1-dev
sudo apt-get install -y libpq-dev
sudo apt-get install -y libmemcached-dev
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
sudo apt-get update
sudo apt-get install -y mongodb-10gen

sudo apt-get build-dep -y python-psycopg2
sudo apt-get install -y binutils 
sudo apt-get install -y libproj-dev 
sudo apt-get install -y gdal-bin
sudo apt-get install -y nginx
sudo apt-get install -y uwsgi



echo "---- Add Repos-----"
sudo add-apt-repository -y ppa:chris-lea/node.js
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >> /etc/apt/sources.list'
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update -qqy	
sudo apt-get install -qq gfortran libatlas-base-dev libjpeg-dev zlib1g-dev python-software-properties ghostscript		
sudo apt-get install -qq memcached
echo "---- postgresql Libs----------"
sudo apt-get install -y postgresql-9.3 
sudo apt-get install -y Postgresql-9.3-postgis
#sudo apt-get install -y postgresql-contrib
#sudo apt-get install -y postgresql-9.1-postgis
#sudo apt-get install -y postgres

echo "---- Downloading Ona.io from Git----------"
sudo mkdir /home/apps/
sudo chmod 775 -R /home/apps/
sudo chown ubuntu:ubuntu /home/apps/
git clone https://github.com/onaio/onadata.git /home/apps/ona

echo "--- Pip installs ------------"
sudo apt-get update
sudo pip install numpy --use-mirrors
sudo pip install flake8
sudo pip install uwsgi
sudo apt-get install -y libevent-dev
sudo apt-get install -y libmemcached-dev
sudo pip install -r /home/apps/ona/requirements/base.pip
sudo pip install -r /home/apps/ona/requirements/latest.pip
sudo pip install -r /home/apps/ona/requirements/dev.pip

## Had to Add POSTGIS_VERSION = (2,1,7)
#virtualenv=/home/vagrant/.virtualenvs/ona

## python manage.py syncdb --noinput
## python manage.py migrate
## python manage.py collectstatic

## ALTER USER postgres WITH PASSWORD 'postgres';

sudo su postgres
createdb onadata_test
psql -c "CREATE EXTENSION IF NOT EXISTS postgis;" -d onadata_test -U postgres
psql -c "CREATE EXTENSION IF NOT EXISTS postgis_topology;" -d onadata_test -U postgres

alter user postgres with password 'QwePoi!23';







