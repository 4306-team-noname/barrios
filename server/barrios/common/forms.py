from django.forms import Form, ModelChoiceField
from data.models import RatesDefinition, UsWeeklyConsumableWaterSummary


class AnalysisForm(Form):
    consumable_name = ModelChoiceField(
        queryset=RatesDefinition.objects.distinct("affected_consumable").exclude(
            affected_consumable="RS Food Rations"
        ),
        empty_label="Select Consumable",
        to_field_name="affected_consumable",
    )
    start_date = ModelChoiceField(queryset=UsWeeklyConsumableWaterSummary.objects.all())
    end_date = ModelChoiceField(queryset=UsWeeklyConsumableWaterSummary.objects.all())
