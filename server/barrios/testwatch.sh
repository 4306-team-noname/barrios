#!/bin/sh

if [[ $# -eq 0 ]]; then
	APP=''
else
	APP=$1
fi

find . -name '*.py' | entr python manage.py test $APP
