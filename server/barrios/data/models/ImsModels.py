from django.db.models import Model
from data.core.managers import EmptyKeywordManager, FlightPlanManager


class ImsModel(Model):
    objects = EmptyKeywordManager()

    class Meta:
        abstract = True


class ImsFlightplanModel(Model):
    objects = FlightPlanManager()

    class Meta:
        abstract = True
