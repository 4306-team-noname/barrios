# from .UserDataEntry import UserDataEntry
from django.db.models import DateField, FloatField, Model


class RsaConsumableWaterSummary(Model):
    report_date = DateField(unique=True)
    remain_potable_liters = FloatField()
    remain_technical_liters = FloatField()
    remain_rodnik_liters = FloatField()

    class Meta:
        db_table = "rsa_consumable_water_summary"
