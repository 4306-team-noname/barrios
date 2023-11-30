import os
import time
from django.core.management.base import BaseCommand, CommandError
from core.settings import MEDIA_ROOT
from data.core.data_dictionary import data_dictionary
from data.core.FieldFileCsvHelper import FieldFileCsvHelper
from data.services import DataService

DATA_PATH = os.path.join(MEDIA_ROOT, "seed_data")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        help = f"Loads the initial dataset for the analysis application. File should be located in {DATA_PATH}"
        print(f"Looking for files in {DATA_PATH}")

        expected_files_readable_names = [
            data_dictionary[key]["readable_name"] for key in data_dictionary.keys()
        ]

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
        num_files = len(file_list)

        if "README.md" in file_list:
            num_files = num_files - 1

        print(f"Attempting to load {num_files} files into the database...")
        for file in file_list:
            if file != "README.md":
                filepath = os.path.join(DATA_PATH, file)
                file_info_result = file_helper.get_file_info(filepath)

                if file_info_result["ok"]:
                    service = DataService(filepath)
                    fileinfo = file_info_result["value"]
                    file_helper.rewrite_csv(filepath, fileinfo["db_fields"])
                    insert_result = service.insert_csv(fileinfo["model_name"])
                    if insert_result["ok"]:
                        print(
                            f"✓ Successfully loaded {fileinfo['readable_name']}:  {file}"
                        )
                        success_files.append(file)
                        if fileinfo["readable_name"] in expected_files_readable_names:
                            expected_files_readable_names.remove(
                                fileinfo["readable_name"]
                            )
                    else:
                        error_files.append(
                            {"filename": file, "error": insert_result["error"]}
                        )
                        print(f"x Error loading file: {file}")
                else:
                    print(f"?? File does not match known data: {file}")
                    bad_files.append(file)

        if len(bad_files) > 0:
            print(
                f"{len(bad_files)} of {num_files} files did not match known data. Please double-check the formatting of the following files:"
            )
            for badfile in bad_files:
                print(badfile)

        if len(error_files) > 0:
            print(
                f"{len(error_files)} of {num_files} files could not be saved to the database. See errors below:"
            )
            for errorfile in error_files:
                print(f"{errorfile['filename']}:: errorfile['error']")

        if len(success_files) > 0:
            print(
                f"{len(success_files)} of {num_files} files were saved to the database successfully."
            )
        if len(expected_files_readable_names) == 0:
            print("All data loaded successfully!\n🙭⭑⭑ Good luck out there! ⭑⭑🙭")
        else:
            for readable_name in expected_files_readable_names:
                print(f"Missing: {readable_name}")
            print(
                f"You need {len(expected_files_readable_names)} more files for everything to work properly."
            )
            print(
                "Load the data manually after starting the server for analysis to work as expected."
            )
        pass
