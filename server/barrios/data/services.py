from csv import DictReader
from cases import to_snake
from common.result import Result
from django.db import connections
import pandas as pd


from .models import (
    Category,
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


class DataService:
    file: str

    def __init__(self, filepath: str = None) -> None:
        if filepath is not None:
            self.file = filepath

    def copy_csv_to_db(self, table_name):
        SQL_STATEMENT = """
            COPY %s FROM STDIN WITH
                CSV
                HEADER
                DELIMITER AS ','
        """
        conn = connections["default"]
        cursor = conn.cursor()
        with open(self.file, "r") as fp:
            next(fp)
            cursor.copy_expert(sql=SQL_STATEMENT % table_name, file=fp)
            conn.commit()
            cursor.close()

    def keys_to_snake(self, model_dict):
        new_dict = {}
        for key in model_dict.keys():
            if "Unnamed" not in key:
                new_dict[to_snake(key)] = model_dict[key]
        return new_dict

    def insert_csv(self, model_name, mapping=None, file_object=None) -> Result:
        result = None
        if model_name == "ImsConsumablesCategoryLookup":
            result = ImsConsumablesCategoryLookup.objects.from_csv(
                self.file, encoding="utf-8"
            )
        elif model_name == "InventoryMgmtSystemConsumables":
            if not file_object:
                result = InventoryMgmtSystemConsumables.objects.from_csv(
                    self.file, encoding="utf-8", mapping=mapping
                )
            else:
                result = InventoryMgmtSystemConsumables.objects.from_csv(
                    file_object, encoding="utf-8", mapping=mapping
                )
        elif model_name == "IssFlightPlan":
            result = IssFlightPlan.objects.from_csv(self.file, encoding="utf-8")
        elif model_name == "IssFlightPlanCrew":
            result = IssFlightPlanCrew.objects.from_csv(self.file, encoding="utf-8")
        elif model_name == "IssFlightPlanCrewNationalityLookup":
            result = IssFlightPlanCrewNationalityLookup.objects.from_csv(
                self.file, encoding="utf-8"
            )
        elif model_name == "RatesDefinition":
            result = RatesDefinition.objects.from_csv(self.file, encoding="utf-8")
        elif model_name == "RsaConsumableWaterSummary":
            result = RsaConsumableWaterSummary.objects.from_csv(
                self.file, encoding="utf-8"
            )
        elif model_name == "TankCapacityDefinition":
            result = TankCapacityDefinition.objects.from_csv(
                self.file, encoding="utf-8"
            )
        elif model_name == "ThresholdsLimitsDefinition":
            result = ThresholdsLimitsDefinition.objects.from_csv(
                self.file, encoding="utf-8"
            )
        elif model_name == "UsRsWeeklyConsumableGasSummary":
            result = UsRsWeeklyConsumableGasSummary.objects.from_csv(
                self.file, encoding="utf-8"
            )
        elif model_name == "UsWeeklyConsumableWaterSummary":
            result = UsWeeklyConsumableWaterSummary.objects.from_csv(
                self.file, encoding="utf-8"
            )
        if result:
            return {"ok": True, "value": result, "error": None}
        else:
            return {
                "ok": False,
                "value": None,
                "error": "There was an error saving your data.",
            }

    def read_and_insert_csv(self, model_name: str, csv_path: str) -> Result:
        # if model_name == 'InventoryMgmtSystemConsumables':

        with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = DictReader(file)
            for row in reader:
                converted = self.keys_to_snake(row)
                result = None

                if model_name == "ImsConsumablesCategoryLookup":
                    result = ImsConsumablesCategoryLookup.objects.create(**converted)
                # elif model_name == "InventoryMgmtSystemConsumables":
                #     result = InventoryMgmtSystemConsumables.objects.create(**converted)
                elif model_name == "IssFlightPlan":
                    result = IssFlightPlan.objects.create(**converted)
                elif model_name == "IssFlightPlanCrew":
                    result = IssFlightPlanCrew.objects.create(**converted)
                elif model_name == "IssFlightPlanCrewNationalityLookup":
                    result = IssFlightPlanCrewNationalityLookup.objects.create(
                        **converted
                    )
                elif model_name == "RatesDefinition":
                    result = RatesDefinition.objects.create(**converted)
                elif model_name == "RsaConsumableWaterSummary":
                    result = RsaConsumableWaterSummary.objects.create(**converted)
                elif model_name == "TankCapacityDefinition":
                    result = TankCapacityDefinition.objects.create(**converted)
                elif model_name == "ThresholdsLimitsDefinition":
                    result = ThresholdsLimitsDefinition.objects.create(**converted)
                elif model_name == "UsRsWeeklyConsumableGasSummary":
                    result = UsRsWeeklyConsumableGasSummary.objects.create(**converted)
                elif model_name == "UsWeeklyConsumableWaterSummary":
                    result = UsWeeklyConsumableWaterSummary.objects.create(**converted)
                if result is not None:
                    return {"ok": True, "value": None, "error": None}
                else:
                    return {
                        "ok": False,
                        "value": None,
                        "error": "Unable to save records",
                    }

    def get_uploaded_file(self, csv_path):
        return pd.read_csv(csv_path, index_col=False, keep_default_na=False)
