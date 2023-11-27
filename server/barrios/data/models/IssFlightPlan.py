from django.db.models import DateField, CharField
from .FlightPlanManager import FlightPlanManager
from data.models import ImsFlightplanModel


class IssFlightPlan(ImsFlightplanModel):
    datedim = DateField()
    vehicle_name = CharField(max_length=255, blank=True, null=True)
    port_name = CharField(max_length=255, blank=True, null=True)
    vehicle_name = CharField(max_length=255, blank=True, null=True)
    vehicle_type = CharField(max_length=255, blank=True, null=True)
    eva_name = CharField(max_length=255, blank=True, null=True)
    eva_type = CharField(max_length=255, blank=True, null=True)
    eva_accuracy = CharField(max_length=255, blank=True, null=True)
    event = CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "iss_flight_plan"
