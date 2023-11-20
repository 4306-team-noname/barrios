from django.core.management.base import BaseCommand, CommandError
from barrios.settings import MEDIA_ROOT
import os

data_path = os.path.join(MEDIA_ROOT, "initial_data/")
