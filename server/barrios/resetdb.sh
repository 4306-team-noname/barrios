#~/bin/sh

# run these two queries in pgadmin
# before running this script
# DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata category
python manage.py createsuperuser
