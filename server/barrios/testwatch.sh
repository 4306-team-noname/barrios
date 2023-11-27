#!/bin/sh
find . -name '*.py' | entr python manage.py test
