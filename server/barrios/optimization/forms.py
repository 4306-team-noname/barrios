from django.forms import ChoiceField, Form
from data.models import (
    RatesDefinition,
    ThresholdsLimitsDefinition,
    UsWeeklyConsumableWaterSummary,
    IssFlightPlan,
)
from datetime import date, datetime


def get_discrete_mission_events():
    # select flight plan entries that are launches and have a date greater than today
    flight_plan_values = IssFlightPlan.objects.filter(
        event="Launch", datedim__gte=date.today()
    ).values("datedim", "vehicle_name")
    mission_events = [
        (
            value["vehicle_name"],
            f"{value['vehicle_name']} — {value['datedim'].strftime('%m/%d/%Y')}",
        )
        for value in flight_plan_values
    ]
    return mission_events


def get_date_range():
    water_summary_dates = UsWeeklyConsumableWaterSummary.objects.all().values("date")
    date_strings = [
        (
            water_date["date"].strftime("%m/%d/%Y"),
            water_date["date"].strftime("%m/%d/%Y"),
        )
        for water_date in water_summary_dates
    ]
    return date_strings


def get_consumable_names():
    thresholds_definitions_values = ThresholdsLimitsDefinition.objects.all().values()
    consumables = []
    for threshold in thresholds_definitions_values:
        if (
            threshold["threshold_category"]
            and threshold["threshold_category"] != "Water Critical"
            and threshold["threshold_owner"] != "RSOS"
        ):
            consumables.append(threshold["threshold_category"])
    consumables = [(consumable, consumable) for consumable in consumables]
    return consumables


class OptimizationForm(Form):
    mission = ChoiceField(choices=get_discrete_mission_events())
    # consumable_name = ChoiceField(choices=get_consumable_names())
