from barrios import settings
from sqlalchemy import create_engine
import pandas as pd
from cases import to_snake


class DataService:
    def __init__(self):
        # setup the database connection
        self.conn_default = create_engine(settings.DB_URI_DEFAULT).connect()
        self.date_fields = {
            "IssFlightPlan": "datedim",
            "IssFlightPlanCrew": "datedim",
            "RsaConsumableWaterSummary": "report_date",
            "UsRsWeeklyConsumableGasSummary": "date",
            "UsWeeklyConsumableWaterSummary": "date",
        }

        self.datetime_fields = {
            "InventoryMgmtSystemConsumables": "datedim",
            "StoredItemsOnlyInventoryMgmtSystemConsumables": "datedim",
        }

    def convert_date_cols(self, model_name: str, df: pd.DataFrame) -> pd.DataFrame:
        if model_name in self.date_fields:
            df[self.date_fields[model_name]] = pd.to_datetime(
                df[self.date_fields[model_name]], format="%m/%d/%Y"
            )
        elif model_name in self.datetime_fields:
            df[self.datetime_fields[model_name]] = pd.to_datetime(
                df[self.datetime_fields[model_name]]
            )
        return df

    def cols_to_snake(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = [to_snake(col) for col in df.columns]
        return df

    def insert_df(self, model_name: str, table_name: str, df: pd.DataFrame):
        df = self.cols_to_snake(df)
        if model_name in self.date_fields.keys() or model_name in self.datetime_fields:
            df = self.convert_date_cols(model_name, df)
        print(df.head())
        rows_affected = df.to_sql(
            table_name,
            self.conn_default,
            index=False,
            if_exists="replace",
            chunksize=25000,
            method=None,
        )
        print(f"rows: {rows_affected}")
