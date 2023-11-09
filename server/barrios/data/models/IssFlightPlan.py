from django.db.models import DateTimeField, CharField, Model

# from .UserDataEntry import UserDataEntry


class IssFlightPlan(Model):
    datedim = DateTimeField()
    vehicle_name = CharField(blank=True)
    port_name = CharField(blank=True)
    vehicle_name = CharField(blank=True)
    eva_name = CharField(blank=True)
    eva_type = CharField(blank=True)
    eva_accuracy = CharField(blank=True)
    event = CharField(blank=True)

    class Meta:
        db_table = "iss_flight_plans"
