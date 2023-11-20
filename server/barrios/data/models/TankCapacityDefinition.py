# from .UserDataEntry import UserDataEntry
from django.db.models import FloatField, CharField, Model

from data.models.EmptyKeywordManager import EmptyKeywordManager


class TankCapacityDefinition(Model):
    tank_category = CharField(unique=True, max_length=255)
    tank_capacity = FloatField()
    units = CharField(max_length=255, blank=True, null=True)

    objects = EmptyKeywordManager()

    class Meta:
        db_table = "tank_capacity_definition"
