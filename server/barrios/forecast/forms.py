from django.forms import DateField, Form


class ForecastForm(Form):
    start_date = DateField()
    end_date = DateField()
