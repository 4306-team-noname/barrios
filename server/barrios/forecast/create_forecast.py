from math import ceil, floor
from random import randint
import pandas as pd
from django.db.models import Q
from data.models import IssFlightPlan, ThresholdsLimitsDefinition
from common.consumable_helpers import get_consumable_thresholds


def create_forecast(consumable_name):
    docking_date_values = IssFlightPlan.objects.filter(event="Dock").values("datedim")
    docking_dates = [d["datedim"] for d in docking_date_values]

    thresholds_object = get_consumable_thresholds(consumable_name)

    dummy_forecast = []
    for docking_date in docking_dates:
        forecast = {
            "date": docking_date,
            consumable_name: randint(
                thresholds_object["min_value"], thresholds_object["max_value"]
            ),
        }
        dummy_forecast.append(forecast)

    forecast_obj = {
        "consumable_name": consumable_name,
        "threshold_value": thresholds_object["threshold_value"],
        "threshold_plus_value": thresholds_object["threshold_plus_value"],
        "critical_value": thresholds_object["critical_value"],
        "min_value": thresholds_object["min_value"],
        "max_value": thresholds_object["max_value"],
        "df": pd.DataFrame(dummy_forecast),
        # TODO: Include actual start date, actual end date,
        # forecast start date, and forecast end date
    }
    return forecast_obj
