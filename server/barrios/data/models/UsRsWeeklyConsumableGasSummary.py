# from .UserDataEntry import UserDataEntry
from django.db.models import DateField, FloatField, Manager, Model
from .CustomFields import EmptyStringToNoneFloatField
from .EmptyKeywordManager import EmptyKeywordManager
from data.models import ImsModel
from datetime import datetime


class UsRsWeeklyConsumableManager(EmptyKeywordManager):
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


class UsRsWeeklyConsumableGasSummary(ImsModel):
    date = DateField(primary_key=True)
    usos_o2_kg = EmptyStringToNoneFloatField()
    rs_o2_kg = EmptyStringToNoneFloatField()
    us_n2_kg = EmptyStringToNoneFloatField()
    rs_n2_kg = EmptyStringToNoneFloatField()
    adjusted_o2_kg = EmptyStringToNoneFloatField()
    adjusted_n2_kg = EmptyStringToNoneFloatField()
    resupply_o2_kg = EmptyStringToNoneFloatField(blank=True, null=True)
    resupply_n2_kg = EmptyStringToNoneFloatField(blank=True, null=True)
    resupply_air_kg = EmptyStringToNoneFloatField(blank=True, null=True)

    objects = UsRsWeeklyConsumableManager()

    class Meta:
        db_table = "us_rs_weekly_consumables_gas_summary"

    def __init__(self, *args, **kwargs):
        print(f"kwargs: {kwargs}")
        super().__init__(*args, **kwargs)
