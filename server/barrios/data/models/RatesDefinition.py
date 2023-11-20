# from .UserDataEntry import UserDataEntry
from django.db.models import FloatField, CharField, Model

from data.models.EmptyKeywordManager import EmptyKeywordManager


class RatesDefinition(Model):
    rate_category = CharField(max_length=255, unique=True)
    affected_consumable = CharField(max_length=255, null=True, blank=True)
    rate = FloatField()
    units = CharField(max_length=255, null=True, blank=True)
    type = CharField(max_length=255, null=True, blank=True)
    efficiency = CharField(max_length=255, null=True, blank=True)

    objects = EmptyKeywordManager()

    class Meta:
        db_table = "rates_definition"
