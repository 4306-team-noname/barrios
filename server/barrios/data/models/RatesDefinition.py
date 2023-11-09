# from .UserDataEntry import UserDataEntry
from django.db.models import RESTRICT, FloatField, ForeignKey, CharField, Model


class RatesDefinition(Model):
    rate_category = ForeignKey("Category", to_field="rate_category", on_delete=RESTRICT)
    affected_consumable = CharField(max_length=200)
    rate = FloatField()
    units = CharField(max_length=200)
    type = CharField(max_length=200)
    efficiency = FloatField()

    class Meta:
        db_table = "rates_definitions"
