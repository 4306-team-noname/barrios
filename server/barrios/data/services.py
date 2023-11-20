from csv import DictReader
from cases import to_snake
from django.db.models import Model
from common.result import Result
from django.db import connections
import pandas as pd
import numpy as np
import subprocess

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

    def get_num_lines(self, csv_path):
        chunk = 1024 * 1024  # Process 1 MB at a time.
        f = np.memmap(csv_path)
        num_newlines = sum(
            np.sum(f[i : i + chunk] == ord("\n")) for i in range(0, len(f), chunk)
        )
        del f
        return num_newlines

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

    def get_uploaded_file(self, csv_path):
        # TODO: Return a result with the dataframe,
        # whether the dataframe is a truncated preview
        # and the total number of rows  in the file
        num_lines = self.get_num_lines(csv_path)
        print(f"num_lines: {num_lines}")

        if num_lines > 10000:
            df = pd.read_csv(
                csv_path, index_col=False, keep_default_na=False, chunksize=10000
            )
            return next(df)
        else:
            df = pd.read_csv(csv_path, index_col=False, keep_default_na=False)
            return df

    def get_model_by_ref(self, ref: str) -> Model:
        model = None
        if ref == "ims_consumables":
            model = InventoryMgmtSystemConsumables
        elif ref == "category_lookup":
            model = ImsConsumablesCategoryLookup
        elif ref == "flight_plan":
            model = IssFlightPlan
        elif ref == "crew_flight_plan":
            model = IssFlightPlanCrew
        elif ref == "crew_nationality_lookup":
            model = IssFlightPlanCrewNationalityLookup
        elif ref == "us_water_summary":
            model = UsWeeklyConsumableWaterSummary
        elif ref == "rsa_water_summary":
            model = RsaConsumableWaterSummary
        elif ref == "weekly_gas_summary":
            model = UsRsWeeklyConsumableGasSummary
        elif ref == "rates_definitions":
            model = RatesDefinition.objects.all()
        elif ref == "tank_capacities":
            model = TankCapacityDefinition
        elif ref == "thresholds_and_limits":
            model = ThresholdsLimitsDefinition
        return model

    def get_data_by_ref(self, ref: str) -> Result:
        results = None
        if ref == "ims_consumables":
            results = InventoryMgmtSystemConsumables.objects.all().order_by("-datedim")
        elif ref == "category_lookup":
            results = ImsConsumablesCategoryLookup.objects.all().order_by("category_id")
        elif ref == "flight_plan":
            results = IssFlightPlan.objects.all().order_by("datedim")
        elif ref == "crew_flight_plan":
            results = IssFlightPlanCrew.objects.all().order_by("datedim")
        elif ref == "crew_nationality_lookup":
            results = IssFlightPlanCrewNationalityLookup.objects.all()
        elif ref == "us_water_summary":
            results = UsWeeklyConsumableWaterSummary.objects.all().order_by("date")
        elif ref == "rsa_water_summary":
            results = RsaConsumableWaterSummary.objects.all().order_by("report_date")
        elif ref == "weekly_gas_summary":
            results = UsRsWeeklyConsumableGasSummary.objects.all().order_by("date")
        elif ref == "rates_definitions":
            results = RatesDefinition.objects.all()
        elif ref == "tank_capacities":
            results = TankCapacityDefinition.objects.all()
        elif ref == "thresholds_and_limits":
            results = ThresholdsLimitsDefinition.objects.all()
        if results is not None:
            return {"ok": True, "value": results, "error": None}
        else:
            return {"ok": False, "value": None, "error": "No results found"}
