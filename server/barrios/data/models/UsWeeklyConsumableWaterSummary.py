# from .UserDataEntry import UserDataEntry
from django.db.models import DateField, FloatField, Model
from .CustomFields import EmptyStringToNoneFloatField
from .EmptyKeywordManager import EmptyKeywordManager
from data.models import ImsModel
from datetime import datetime


class UsWeeklyConsumableManager(EmptyKeywordManager):
    def create(self, *args, **kwargs):
        newargs = {}
        for key in kwargs.keys():
            if key == "date":
                if len(kwargs[key]) > 0:
                    newargs[key] = datetime.strptime(kwargs[key], "%m/%d/%Y").date()
                else:
                    newargs[key] = None
            else:
                newargs[key] = kwargs[key]

        super().create(*args, **newargs)


class UsWeeklyConsumableWaterSummary(ImsModel):
    date = DateField(primary_key=True)
    corrected_potable_l = EmptyStringToNoneFloatField()
    corrected_technical_l = EmptyStringToNoneFloatField()
    corrected_total_l = EmptyStringToNoneFloatField()
    resupply_potable_l = EmptyStringToNoneFloatField(blank=True, null=True)
    resupply_technical_l = EmptyStringToNoneFloatField(blank=True, null=True)
    corrected_predicted_l = EmptyStringToNoneFloatField()

    objects = UsWeeklyConsumableManager()

    class Meta:
        db_table = "us_weekly_consumable_water_summary"
