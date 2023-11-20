# from .UserDataEntry import UserDataEntry
from django.db.models import CharField, BooleanField, Model

from data.models.EmptyKeywordManager import EmptyKeywordManager


class IssFlightPlanCrewNationalityLookup(Model):
    nationality = CharField(primary_key=True, unique=True)
    is_usos_crew = BooleanField()
    is_rsa_crew = BooleanField()

    objects = EmptyKeywordManager()

    class Meta:
        db_table = "iss_flight_plan_crew_nationality_lookup"
