#!/bin/bash -x
PWD=`pwd`
/usr/bin/virtualenv --python=python venv
echo $PWD
activate () {
    . $PWD/venv/bin/activate;
    pip install -r requirements.txt
}

activate
cp ~/*.json ./client_secret.json
python main.py