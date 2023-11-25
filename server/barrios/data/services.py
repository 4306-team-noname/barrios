from __future__ import annotations
from cases import to_snake
from common.result import Result
import pandas as pd
import numpy as np
from data.core.import_csv import import_csv

from data.models import (
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

    def __init__(self, filepath: str | None = None) -> None:
        if filepath is not None:
            self.file = filepath

    def get_num_lines(self, csv_path):
        """
        Returns the number of lines in a csv file
        located at the given file path
        :param csv_path: str
            The path to a csv file

        :return int:
            The number of lines in a csv file
        """
        chunk = 1024 * 1024  # Process 1 MB at a time.
        f = np.memmap(csv_path)
        num_newlines = sum(
            np.sum(f[i : i + chunk] == ord("\n")) for i in range(0, len(f), chunk)
        )
        del f
        return num_newlines

    def keys_to_snake(self, original_dict):
        """Create a copy of the given dict with keys
           converted to snake_case.

        :param original_dict: dict[Any]:
            The dict whose keys need to be converted to
            snake_case.

        :returns: dict[Any]:
            A copy of "original_dict" with snake_case keys
        """
        new_dict = {}
        for key in original_dict.keys():
            if "Unnamed" not in key:
                new_dict[to_snake(key)] = original_dict[key]
        return new_dict

    def insert_csv(self, model_name: str, file_object=None) -> Result:
        """Inserts all rows of the given csv file into the database.

        Params
        ------
        model_name : str
            The name of the model to insert
        file_object : File
            A csv file object
        """
        return import_csv(model_name, self.file)

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

    def get_count_by_slug(self, slug: str) -> int:
        model = None
        if slug == "ims_consumables":
            model = InventoryMgmtSystemConsumables
        elif slug == "category_lookup":
            model = ImsConsumablesCategoryLookup
        elif slug == "flight_plan":
            model = IssFlightPlan
        elif slug == "crew_flight_plan":
            model = IssFlightPlanCrew
        elif slug == "crew_nationality_lookup":
            model = IssFlightPlanCrewNationalityLookup
        elif slug == "us_water_summary":
            model = UsWeeklyConsumableWaterSummary
        elif slug == "rsa_water_summary":
            model = RsaConsumableWaterSummary
        elif slug == "weekly_gas_summary":
            model = UsRsWeeklyConsumableGasSummary
        elif slug == "rates_definitions":
            model = RatesDefinition
        elif slug == "tank_capacities":
            model = TankCapacityDefinition
        elif slug == "thresholds_and_limits":
            model = ThresholdsLimitsDefinition
        if model:
            return model.objects.count()
        else:
            return 0

    def get_data_by_slug(self, slug: str) -> Result:
        """
        Retrieves all IMS-related records associated with a slug.
        :param slug: str:
            The slug, defined in the data dictionary,
            for the model to retrieve
        :returns Result[Queryset]:
            Any records associated with the given slug
        """
        results = None
        name = None
        if slug == "ims_consumables":
            results = InventoryMgmtSystemConsumables.objects.all().order_by("-datedim")
            name = "IMS Consumables"
        elif slug == "category_lookup":
            results = ImsConsumablesCategoryLookup.objects.all().order_by("category_id")
            name = "Category Lookup"
        elif slug == "flight_plan":
            results = IssFlightPlan.objects.all().order_by("datedim")
            name = "Flight Plan"
        elif slug == "crew_flight_plan":
            results = IssFlightPlanCrew.objects.all().order_by("datedim")
            name = "Crew Flight Plan"
        elif slug == "crew_nationality_lookup":
            results = IssFlightPlanCrewNationalityLookup.objects.all()
            name = "Crew Nationality Lookup"
        elif slug == "us_water_summary":
            results = UsWeeklyConsumableWaterSummary.objects.all().order_by("date")
            name = "US Water Summary"
        elif slug == "rsa_water_summary":
            results = RsaConsumableWaterSummary.objects.all().order_by("report_date")
            name = "RSA Water Summary"
        elif slug == "weekly_gas_summary":
            results = UsRsWeeklyConsumableGasSummary.objects.all().order_by("date")
            name = "Weekly Gas Summary"
        elif slug == "rates_definitions":
            results = RatesDefinition.objects.all()
            name = "Rates Definitions"
        elif slug == "tank_capacities":
            results = TankCapacityDefinition.objects.all()
            name = "Tank Capacities"
        elif slug == "thresholds_and_limits":
            results = ThresholdsLimitsDefinition.objects.all()
            name = "Thresholds and Limits"
        if results is not None:
            return {"ok": True, "value": {"data": results, "name": name}, "error": None}
        else:
            return {"ok": False, "value": None, "error": "No results found"}
