# from .UserDataEntry import UserDataEntry
from django.db.models import CASCADE, DateTimeField, ForeignKey, IntegerField, Model
from .IssFlightPlanCrewNationalityLookup import IssFlightPlanCrewNationalityLookup


class IssFlightPlanCrew(Model):
    datedim = DateTimeField()
    nationality_category = ForeignKey(
        IssFlightPlanCrewNationalityLookup, on_delete=CASCADE
    )
    crew_count = IntegerField()

    class Meta:
        db_table = "iss_flight_plan_crews"
