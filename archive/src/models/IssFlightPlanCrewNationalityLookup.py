from emmett.orm import Model, Field, has_many


class IssFlightPlanCrewNationalityLookup(Model):
    tablename = "iss_flight_plan_crew_nationality_lookup"
    primary_keys = ["nationality"]

    nationality = Field.text(unique=True)
    is_usos_crew = Field.int()
    is_rsa_crew = Field.int()

    validation = {
        "nationality": {"presence": True},
        "is_usos_crew": {"presence": True},
        "is_rsa_crew": {"presence": True},
    }
