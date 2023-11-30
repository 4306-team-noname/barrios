from django.forms import DateField, Form


class UsageForm(Form):
    start_date = DateField()
    end_date = DateField()
