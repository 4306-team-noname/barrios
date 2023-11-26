import os
from django.core.management.base import BaseCommand, CommandError
from barrios.settings import MEDIA_ROOT
from data.core.data_dictionary import data_dictionary

from data.models import (
    Category,
    Consumable,
    ImsConsumablesCategoryLookup,
    InventoryMgmtSystemConsumables,
    IssFlightPlan,
    IssFlightPlanCrew,
    IssFlightPlanCrewNationalityLookup,
    RatesDefinition,
    RsaConsumableWaterSummary,
    TankCapacityDefinition,
    ThresholdsLimitsDefinition,
    UsRsWeeklyConsumableGasSummary,
    UsWeeklyConsumableWaterSummary,
)

DATA_PATH = os.path.join(MEDIA_ROOT, "seed_data")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        help = f"Loads the initial dataset for the analysis application. File should be located in {DATA_PATH}"
        print(f"Looking for files in {DATA_PATH}")

        expected_files_readable_names = [
            data_dictionary[key]["readable_name"] for key in data_dictionary.keys()
        ]

        found_files_readable_names = []

        print(f"expecting: {expected_files_readable_names}")

        file_list = [
            file
            for file in os.listdir(DATA_PATH)
            if os.path.isfile(os.path.join(DATA_PATH, file))
        ]

        if len(file_list) == 0:
            raise CommandError(f"No files found in {DATA_PATH}")

        for file in file_list:
            if file != "README.md":
                print(f" ✓ {file}")

        # 1. Read the contents of a predefined folder
        # 2. For each file:
        #   -Check if the file matches something
        #    in the data dictionary
        #   -If yes, add the data
        #   -If no, print that the file is unknown
        # 3. Keep a list of models inserted into the db
        #   -If any models are missing, warn the user
        pass
