from emmett.orm import Model, Field


class IssFlightPlanCrew(Model):
    tablename = 'iss_flight_plan_crew'

    datedim = Field.date()
    nationality_category = Field.text()
    crew_count = Field.int()

    validation = {
        'datedim': {'presence': True},
        'nationality_category': {'presence': True},
        'crew_count': {'presence': True},
    }

