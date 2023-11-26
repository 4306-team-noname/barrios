import pandas as pd
from common.result import Result


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
