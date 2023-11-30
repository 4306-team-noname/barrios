from django.forms import DateField, ChoiceField, Form


class UsageForm(Form):
    start_date = DateField()
    end_date = DateField()
