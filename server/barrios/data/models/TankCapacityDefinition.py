# from .UserDataEntry import UserDataEntry
from django.db.models import FloatField, CharField, Model
from data.models import ImsModel


class TankCapacityDefinition(ImsModel):
    tank_category = CharField(unique=True, max_length=255)
    tank_capacity = FloatField()
    units = CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "tank_capacity_definition"
