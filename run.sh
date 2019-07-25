#!/bin/bash -x
PWD=`pwd`
/usr/bin/virtualenv --python=python venv
echo $PWD
activate () {
    . $PWD/venv/bin/activate;
    pip install -r requirements.txt
}

activate
. ~/init.sh
python main.py