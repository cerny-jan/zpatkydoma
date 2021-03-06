#!/bin/sh

# This script should be executed remotely on the production machine.
if [ "$USER" != "app" ]; then
    exit
fi

# clear existing source code
rm -rf /srv/app

# get latest code
git clone --progress --depth=1 --branch=master https://github.com/cerny-jan/zpatkydoma  /srv/app

# set permissions
chmod 764 /srv/app/deployment/update.sh

# install dependencies
/srv/venv/bin/pip install -U pip
/srv/venv/bin/pip install -r /srv/app/requirements.txt

# run django after deploy commands
supervisorctl restart django-deploy:*
# restart the app
supervisorctl restart app
