from django.forms import Form, ModelChoiceField
from data.models import IssFlightPlan, RatesDefinition
from datetime import date


class OptimizationForm(Form):
    consumable = ModelChoiceField(
        queryset=RatesDefinition.objects.order_by("affected_consumable")
        .distinct("affected_consumable")
        .values("affected_consumable"),
        empty_label="Select Consumable",
        to_field_name="affected_consumable",
    )
    # mission = ModelChoiceField(
    #     queryset=IssFlightPlan.objects.filter(
    #         event="Launch", datedim__gte=date.today()
    #     ),
    #     empty_label="Select Mission",
    #     to_field_name="vehicle_name",
    # )
