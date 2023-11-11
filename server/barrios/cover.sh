#!/bin/sh

set -e

if [[ $# -eq 0 ]]; then
	APP=''
else
	APP=$1
fi

coverage erase
coverage run manage.py test ${APP}
coverage report
