# from .UserDataEntry import UserDataEntry
from django.db.models import CharField, DateField, IntegerField, Model
from data.models import ImsFlightplanModel


class IssFlightPlanCrew(ImsFlightplanModel):
    datedim = DateField()
    nationality_category = CharField(max_length=255, blank=True, null=True)
    crew_count = IntegerField()

    # NOTE: spread country column into multiple
    # columns with the same datedim. Will make it easier
    # to query how many people will be on station.

    readable_name = "Flight Plan Crew"

    class Meta:
        db_table = "iss_flight_plan_crew"
