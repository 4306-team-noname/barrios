from math import ceil, floor
from random import randint
import pandas as pd
from django.db.models import Q
from data.models import IssFlightPlan, ThresholdsLimitsDefinition


def create_forecast(consumable_name):
    docking_date_values = IssFlightPlan.objects.filter(event="Dock").values("datedim")
    docking_dates = [d["datedim"] for d in docking_date_values]

    critical_value = None

    if consumable_name == "water":
        water_values = ThresholdsLimitsDefinition.objects.filter(
            Q(threshold_category="Water Alert") | Q(threshold_category="Water Critical")
        ).values()
        threshold = water_values[0]
        critical_value = water_values[1]["threshold_value"]
    else:
        threshold = list(
            ThresholdsLimitsDefinition.objects.filter(
                threshold_category=consumable_name
            ).values()
        )[0]

    threshold_value = threshold["threshold_value"]
    threshold_plus_value = threshold_value + threshold_value * 0.1

    max_value = int(ceil(threshold_value * 1.25))
    min_value = int(floor(threshold_plus_value * 0.9))

    dummy_forecast = []
    for docking_date in docking_dates:
        forecast = {
            "date": docking_date,
            consumable_name: randint(min_value, max_value),
        }
        dummy_forecast.append(forecast)

    forecast_obj = {
        "consumable_name": consumable_name,
        "threshold_value": threshold_value,
        "threshold_plus_value": threshold_plus_value,
        "critical_value": critical_value,
        "min_value": min_value,
        "max_value": max_value,
        "df": pd.DataFrame(dummy_forecast),
        # TODO: Include actual start date, actual end date,
        # forecast start date, and forecast end date
    }
    return forecast_obj
