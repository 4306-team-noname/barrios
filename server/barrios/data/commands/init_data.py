import os
from django.core.management.base import BaseCommand, CommandError
from barrios.settings import MEDIA_ROOT
from data.core.import_csv import import_csv

data_path = os.path.join(MEDIA_ROOT, "initial_data/")

class Command(BaseCommand):
    help = "Initializes the database with IMS datasets. Files must be stored in /server/barrios/media/initial_data"

    def handle(self, *args, **kwargs):
        
