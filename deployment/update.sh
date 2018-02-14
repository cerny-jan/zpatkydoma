#!/bin/sh

# Update of app source code, dependencies installation, app restart

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
/srv/venv/bin/pip install -r requirements.txt

# restart the app
supervisorctl restart app
