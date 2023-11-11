#!/bin/sh

set -e

if [[ $# -eq 0 ]]; then
	APP=''
else
	APP=$1
fi

python manage.py test ${APP} -v 2
