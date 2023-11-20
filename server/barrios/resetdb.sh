#~/bin/sh
ADMIN_USERNAME=admin
ADMIN_EMAIL=jcaldwell2+barriosadmin@angelo.edu

python manage.py flush
# run these two queries in pgadmin
# before running this script
# DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

rm media/uploads/*

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata category
python manage.py createsuperuser --username $ADMIN_USERNAME --email $ADMIN_EMAIL
