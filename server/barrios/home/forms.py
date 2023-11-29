from django.forms import DateField, ChoiceField, Form


class AnalysisForm(Form):
    CHOICES = (
        ("Usage", "Usage"),
        ("Optimization", "Optimization"),
        ("Forecast", "Forecast"),
    )
    analysis_type = ChoiceField(choices=CHOICES)


class ForecastForm(Form):
    start_date = DateField()
    end_date = DateField()
