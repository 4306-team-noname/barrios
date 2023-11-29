import pandas as pd
import numpy as np
from common.result import Result
from data.core.data_dictionary import data_dictionary


class FieldFileCsvHelper:
    def rewrite_csv(self, filepath: str, fieldnames: list[str]) -> Result:
        """Rewrites a csv file — located on the filesystem — without 'Unnamed' fields

        Params
        ------
        filepath : str
            The path to the file
        fieldnames : str
            A list of fieldnames to use as the output file's header
        """
        try:
            df = pd.read_csv(
                filepath,
                header=0,
                names=fieldnames,
                index_col=False,
                keep_default_na=False,
                low_memory=False,
            )
            # drop unnamed columns
            df = df.loc[:, ~df.columns.str.match("Unnamed")]
            df.to_csv(filepath, index=False, chunksize=5000)
            return {"ok": True, "value": None, "error": None}
        except FileNotFoundError as e:
            return {"ok": False, "value": None, "error": str(e)}

    def get_csv_header(self, filepath):
        df = pd.read_csv(filepath, index_col=False, nrows=0)
        df = df.loc[:, ~df.columns.str.match("Unnamed")]
        return df.columns.tolist()

    def get_csv_column_dtypes(self, filepath):
        df = pd.read_csv(filepath, index_col=False, nrows=1)
        df = df.loc[:, ~df.columns.str.match("Unnamed")]
        # print([str(t) for t in df.dtypes])
        return [str(t) for t in df.dtypes]

    def get_file_info(self, filepath):
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
        file_cols = self.get_csv_header(filepath)
        file_dtypes = self.get_csv_column_dtypes(filepath)
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
            file_dtypes_match = np.array_equal(
                file_dtypes_arr, dictionary_entry_dtypes_arr
            )

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
