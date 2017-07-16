#!/bin.bash
# Needs:
# * README.md
# * .gitignore
# * requirements.txt
PROJECT_NAME=movies
git branch staging && git push --set-upstream origin staging
git branch develop && git push --set-upstream origin develop
git checkout -b ft-api && git push --set-upstream origin ft-api
#python3 -m venv venv
# for python 3.3:
virtualenv --python=python3 venv
source venv/bin/activate
pip3 -V
pip3 install -r requirements.txt
venv/lib/python3.4/site-packages/django/bin/django-admin.py startproject $PROJECT_NAME
cd $PROJECT_NAME
./manage.py startapp api
./manage.py check

# heroku git:clone -a myapp
# heroku config:set DJANGO_SETTINGS_MODULE=settings.production
