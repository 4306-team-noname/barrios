from django.db.models import CharField, BooleanField, Model
from data.models import ImsFlightplanModel


class IssFlightPlanCrewNationalityLookup(ImsFlightplanModel):
    nationality = CharField(primary_key=True, unique=True)
    is_usos_crew = BooleanField()
    is_rsa_crew = BooleanField()

    class Meta:
        db_table = "iss_flight_plan_crew_nationality_lookup"
