from emmett.orm import Model, Field, belongs_to
class FlightPlanEntry(Model):
    belongs_to('upload')
    datedim = Field.date()
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