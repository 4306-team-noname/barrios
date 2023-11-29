import os
from django.core.management.base import BaseCommand, CommandError
from core.settings import MEDIA_ROOT
from data.core.data_dictionary import data_dictionary
from data.core.FieldFileCsvHelper import FieldFileCsvHelper
from data.services import DataService


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

        file_helper = FieldFileCsvHelper()
        bad_files = []
        error_files = []
        success_files = []

        for file in file_list:
            if file != "README.md":
                filepath = os.path.join(DATA_PATH, file)
                file_info_result = file_helper.get_file_info(filepath)

                if not file_info_result["ok"]:
                    print(f"?? File does not match known data: {file}")
                    bad_files.append(file)

                service = DataService(filepath)
                fileinfo = file_info_result["value"]

                file_helper.rewrite_csv(filepath, fileinfo["db_fields"])
                insert_result = service.insert_csv(fileinfo["model_name"])

                if not insert_result["ok"]:
                    error_files.append(
                        {"filename": file, "error": insert_result["error"]}
                    )
                    print(f"x Error loading file: {file}")
                else:
                    print(f"✓ Successfully loaded file:  {file}")
                    success_files.append(file)

        if len(bad_files) > 0:
            print(
                f"{len(bad_files)} of your files did not match known data. Please double-check the formatting of files listed above."
            )

        if len(error_files) > 0:
            print(
                f"len(error_files) of your files could not be saved to the database. See the errors above."
            )

        if len(success_files) > 0:
            print(
                f"len(success_files) of your files were saved to the database successfully."
            )

        # 1. Read the contents of a predefined folder
        # 2. For each file:
        #   -Check if the file matches something
        #    in the data dictionary
        #   -If yes, add the data
        #   -If no, print that the file is unknown
        # 3. Keep a list of models inserted into the db
        #   -If any models are missing, warn the user
        pass
