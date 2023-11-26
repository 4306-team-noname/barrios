from data.core.data_dictionary import data_dictionary
from data.core.FieldFileCsvHelper import FieldFileCsvHelper
from data.core.mappings import mappings
import numpy as np
from common.result import Result


def get_file_info(filepath: str) -> Result:
    """Returns data dictionary information about the file located at the given filepath.
    Parameters
    ----------
    filepath : str
        The path the the csv file

    Returns
    -------
    Result
        The result of looking up the given csv file in the predefined data dictionary.
        {
            'ok': boolean,
            'value': None | {
                "model_name": str,
                "file_fields": list[str],
                "db_fields": list[str],
                "readable_name": str,
                "slug": str,
            },
            'error': None | str
        }
    """
    file_cols = FieldFileCsvHelper().get_csv_header(filepath)
    file_dtypes = FieldFileCsvHelper().get_csv_column_dtypes(filepath)
    file_cols_arr = np.asarray(file_cols)
    file_dtypes_arr = np.asarray(file_dtypes)

    for key in data_dictionary.keys():
        # Check each entry in the data_dictionary against
        # the column names and dtypes of the given csv file.
        # If there's a match between the column names or types,
        # we can assume the csv should be handled by the model
        # specified in the data dictionary.
        dictionary_entry = data_dictionary[key]
        dictionary_file_cols_arr = np.asarray(dictionary_entry["file_columns"])
        dictionary_db_cols_arr = np.asarray(dictionary_entry["database_columns"])
        dictionary_entry_dtypes_arr = np.asarray(
            dictionary_entry["dataframe_column_types"]
        )

        file_cols_match = np.array_equal(file_cols_arr, dictionary_file_cols_arr)
        db_cols_match = np.array_equal(file_cols_arr, dictionary_db_cols_arr)
        file_dtypes_match = np.array_equal(file_dtypes_arr, dictionary_entry_dtypes_arr)

        if (
            file_cols_match is True
            or db_cols_match is True
            or file_dtypes_match is True
        ):
            model_name = dictionary_entry["model_name"]
            return {
                "ok": True,
                "value": {
                    "model_name": model_name,
                    "file_fields": file_cols,  # original file fields
                    "db_fields": dictionary_entry[
                        "database_columns"
                    ],  # database fields
                    "readable_name": dictionary_entry["readable_name"],
                    "slug": dictionary_entry["slug"],
                },
                "error": None,
            }
    # no matches, return error result
    return {
        "ok": False,
        "value": None,
        "error": "File fields did not match a known database table",
    }
