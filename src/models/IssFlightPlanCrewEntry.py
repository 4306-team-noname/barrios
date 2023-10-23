from emmett.orm import Model, Field, belongs_to

class IssFlightPlanCrewEntry(Model):
    tablename = 'iss_flight_plan_crew'
    
    belongs_to('upload')
    datedim = Field.date()
    nationality_category = Field.text()
    crew_count = Field.int()

    validation = {
        'datedim': {'presence': True},
        'nationality_category': {'presence': True},
        'crew_count': {'presence': True},
    }