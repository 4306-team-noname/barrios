# from .UserDataEntry import UserDataEntry
from django.db.models import CharField, DateField, IntegerField, Model


class IssFlightPlanCrew(Model):
    datedim = DateField()
    nationality_category = CharField(max_length=200)
    crew_count = IntegerField()

    # NOTE: spread country column into multiple
    # columns with the same datedim. Will make it easier
    # to query how many people will be on station.

    class Meta:
        db_table = "iss_flight_plan_crew"
