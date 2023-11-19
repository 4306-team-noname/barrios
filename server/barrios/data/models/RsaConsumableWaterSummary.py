# from .UserDataEntry import UserDataEntry
from django.db.models import DateField, FloatField, Model
from .EmptyKeywordManager import EmptyKeywordManager
from datetime import datetime


class RsaConsumablesManager(EmptyKeywordManager):
    def create(self, *args, **kwargs):
        newargs = {}
        for key in kwargs.keys():
            if key == "report_date":
                if len(kwargs[key]) > 0:
                    newargs[key] = datetime.strptime(kwargs[key], "%m/%d/%Y").date()
                else:
                    newargs[key] = None
            else:
                newargs[key] = kwargs[key]

        super().create(*args, **newargs)


class RsaConsumableWaterSummary(Model):
    report_date = DateField(primary_key=True)
    remain_potable_liters = FloatField()
    remain_technical_liters = FloatField()
    remain_rodnik_liters = FloatField()

    objects = RsaConsumablesManager()

    class Meta:
        db_table = "rsa_consumable_water_summary"
