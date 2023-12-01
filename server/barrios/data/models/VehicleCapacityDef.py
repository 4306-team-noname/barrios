from django.db.models import Model, CharField, FloatField, IntegerField
from data.core.managers import EmptyKeywordManager


class VehicleCapacityDef(Model):
    vehicle = CharField(max_length=255)
    ascent_capacity_ctbe = IntegerField(blank=True, null=True)
    descent_capacity_ctbe = IntegerField(blank=True, null=True)
    trash_capacity_ctbe = IntegerField(blank=True, null=True)
    total_capacity_ctbe = FloatField(blank=True, null=True)

    objects = EmptyKeywordManager()

    class Meta:
        db_table = "vehicle_capacity_def"
