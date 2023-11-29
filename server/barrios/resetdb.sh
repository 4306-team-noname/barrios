#!/usr/bin/env bash

# IMPORTANT
# ---------
# This script will wipe all data from
# the database associated with this application!
#
# DO NOT RUN THIS SCRIPT IN PRODUCTION OR
# YOU WILL LOSE ALL OF YOUR DATA!
#
# Prerequisites:
# -------------
# Run the following queries in your db management
# tool of choice before running this script:
# DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;
# GRANT ALL ON SCHEMA public TO postgres;
# GRANT ALL ON SCHEMA public TO public;

# Set your first superuser credentials
# here:
ADMIN_USERNAME=admin
ADMIN_EMAIL=jcaldwell2+barriosadmin@angelo.edu

# Remove all preexisting records from the database.
python manage.py flush

# Remove all previous migration files
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

# remove previously uploaded files
# from the media folder
rm media/uploads/*

# migrate
python manage.py makemigrations
python manage.py migrate

# Preload categories into the database
python manage.py loaddata category

# Create the superuser with the credentials defined above
python manage.py createsuperuser --username $ADMIN_USERNAME --email $ADMIN_EMAIL
