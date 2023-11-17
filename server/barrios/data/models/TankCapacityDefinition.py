# from .UserDataEntry import UserDataEntry
from django.db.models import FloatField, CharField, Model


class TankCapacityDefinition(Model):
    tank_category = CharField(unique=True, max_length=200)
    tank_capacity = FloatField()
    units = CharField(max_length=200)

    class Meta:
        db_table = "tank_capacity_definition"
