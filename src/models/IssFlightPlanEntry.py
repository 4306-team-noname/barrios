from emmett.orm import Model, Field, belongs_to

class IssFlightPlanEntry(Model):
    tablename = 'iss_flight_plan'
    belongs_to('upload')
    datedim = Field.text()
    vehicle_name = Field.text()
    port_name = Field.text()
    vehicle_type = Field.text()
    eva_name = Field.text()
    eva_type = Field.text()
    eva_accuracy = Field.text()
    event = Field.text()
    
    validation = {
        'datedim': {'presence': True}
    }