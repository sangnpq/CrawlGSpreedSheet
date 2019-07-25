#!/bin/bash -x
PWD=`pwd`
/usr/bin/virtualenv --python=python venv
echo $PWD
activate () {
    source $PWD/venv/bin/activate
}

activate
sudo pip install -r requirements.txt
cp ~/*.json ./client_secret.json
python main.py