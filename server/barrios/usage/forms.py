from django.forms import Form, ModelChoiceField
from data.models import RatesDefinition, UsWeeklyConsumableWaterSummary


class UsageForm(Form):
    start_date = ModelChoiceField(queryset=UsWeeklyConsumableWaterSummary.objects.all())
    end_date = ModelChoiceField(queryset=UsWeeklyConsumableWaterSummary.objects.all())
    consumable_name = ModelChoiceField(queryset=RatesDefinition.objects.all())
