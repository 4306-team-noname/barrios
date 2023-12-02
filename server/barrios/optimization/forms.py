from django.forms import Form, ModelChoiceField
from data.models import (
    IssFlightPlan,
)
from datetime import date


class OptimizationForm(Form):
    mission = ModelChoiceField(
        queryset=IssFlightPlan.objects.filter(
            event="Launch", datedim__gte=date.today()
        ).values("datedim", "vehicle_name")
    )
