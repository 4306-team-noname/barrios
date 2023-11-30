from django.forms import DateField, Form


class OptimizationForm(Form):
    start_date = DateField()
    end_date = DateField()
