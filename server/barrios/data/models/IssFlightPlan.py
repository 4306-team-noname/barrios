from django.db.models import DateField, CharField, Model


class IssFlightPlan(Model):
    datedim = DateField()
    vehicle_name = CharField(blank=True)
    port_name = CharField(blank=True)
    vehicle_name = CharField(blank=True)
    vehicle_type = CharField(blank=True)
    eva_name = CharField(blank=True)
    eva_type = CharField(blank=True)
    eva_accuracy = CharField(blank=True)
    event = CharField(blank=True)

    # NOTE: days_until_next_launch:
    # computed field?

    class Meta:
        db_table = "iss_flight_plan"
