# from .UserDataEntry import UserDataEntry
from django.db.models import FloatField, CharField, Model


class RatesDefinition(Model):
    rate_category = CharField(max_length=200, unique=True)
    affected_consumable = CharField(max_length=200)
    rate = FloatField()
    units = CharField(max_length=200)
    type = CharField(max_length=200)
    efficiency = CharField(null=True, blank=True)

    class Meta:
        db_table = "rates_definition"
