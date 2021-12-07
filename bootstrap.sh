#!/bin/sh

#export FLASK_APP=./cashman/index.py
export FLASK_APP=./cashman
export FLASK_DEBUG=1

#source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0

