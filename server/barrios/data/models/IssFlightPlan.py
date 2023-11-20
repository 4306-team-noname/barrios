from django.db.models import DateField, CharField, Model
from .FlightPlanManager import FlightPlanManager


class IssFlightPlan(Model):
    datedim = DateField()
    vehicle_name = CharField(max_length=255, blank=True, null=True)
    port_name = CharField(max_length=255, blank=True, null=True)
    vehicle_name = CharField(max_length=255, blank=True, null=True)
    vehicle_type = CharField(max_length=255, blank=True, null=True)
    eva_name = CharField(max_length=255, blank=True, null=True)
    eva_type = CharField(max_length=255, blank=True, null=True)
    eva_accuracy = CharField(max_length=255, blank=True, null=True)
    event = CharField(max_length=255, blank=True, null=True)

    objects = FlightPlanManager()

    # NOTE: days_until_next_launch:
    # computed field?

    class Meta:
        db_table = "iss_flight_plan"
