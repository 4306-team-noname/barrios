from django.db.models import DateField, CharField, Model
from .FlightPlanManager import FlightPlanManager
from datetime import datetime


class IssFlightPlan(Model):
    datedim = DateField(primary_key=True)
    vehicle_name = CharField(blank=True)
    port_name = CharField(blank=True)
    vehicle_name = CharField(blank=True)
    vehicle_type = CharField(blank=True)
    eva_name = CharField(blank=True)
    eva_type = CharField(blank=True)
    eva_accuracy = CharField(blank=True)
    event = CharField(blank=True)

    objects = FlightPlanManager()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    # NOTE: days_until_next_launch:
    # computed field?

    class Meta:
        db_table = "iss_flight_plan"
