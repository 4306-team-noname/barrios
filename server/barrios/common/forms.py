from django.forms import ChoiceField, Form
from data.models import RatesDefinition, UsWeeklyConsumableWaterSummary


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
    rates_definitions_values = RatesDefinition.objects.all().values()
    consumables = []
    for rate in rates_definitions_values:
        if (
            rate["affected_consumable"]
            and rate["affected_consumable"] not in consumables
            and rate["type"] != "generation"
        ):
            consumables.append(rate["affected_consumable"])
    consumables = [(consumable, consumable) for consumable in consumables]
    print(consumables)
    return consumables


class AnalysisForm(Form):
    start_date = ChoiceField(choices=get_date_range())
    end_date = ChoiceField(choices=get_date_range())
    consumable_name = ChoiceField(choices=get_consumable_names())
