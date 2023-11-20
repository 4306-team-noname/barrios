import pandas as pd


class FieldFileCsvHelper:
    def rewrite_csv(self, filepath: str, fieldnames: list[str]):
        # NOTE: parse_dates?
        # (see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas-read-csv)
        df = pd.read_csv(
            filepath,
            header=0,
            names=fieldnames,
            index_col=False,
            keep_default_na=False,
            low_memory=False,
        )
        df = df.loc[:, ~df.columns.str.match("Unnamed")]
        file_result = df.to_csv(filepath, index=False, chunksize=5000)
        # TODO: Return result object

    def get_csv_header(self, filepath):
        df = pd.read_csv(filepath, index_col=False, nrows=0)
        df = df.loc[:, ~df.columns.str.match("Unnamed")]
        return df.columns.tolist()
