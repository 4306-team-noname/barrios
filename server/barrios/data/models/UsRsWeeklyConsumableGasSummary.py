# from .UserDataEntry import UserDataEntry
from django.db.models import DateField, FloatField, Model


class UsRsWeeklyConsumableGasSummary(Model):
    date = DateField()
    usos_o2_kg = FloatField()
    rs_o2_kg = FloatField()
    us_n2_kg = FloatField()
    rs_n2_kg = FloatField()
    adjusted_o2_kg = FloatField()
    adjusted_n2_kg = FloatField()
    resupply_o2_kg = FloatField(blank=True, null=True)
    resupply_n2_kg = FloatField(blank=True, null=True)
    resupply_air_kg = FloatField(blank=True, null=True)

    class Meta:
        db_table = "us_rs_weekly_consumables_gas_summary"
