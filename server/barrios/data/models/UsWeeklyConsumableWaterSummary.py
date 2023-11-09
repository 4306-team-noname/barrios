# from .UserDataEntry import UserDataEntry
from django.db.models import DateField, FloatField, Model


class UsWeeklyConsumableWaterSummary(Model):
    date = DateField(primary_key=True)
    corrected_potable_l = FloatField()
    corrected_technical_l = FloatField()
    corrected_total_l = FloatField()
    resupply_potable_l = FloatField(blank=True, null=True)
    resupply_technical_l = FloatField(blank=True, null=True)
    corrected_predicted_l = FloatField()

    class Meta:
        db_table = "us_weekly_consumable_water_summary"
