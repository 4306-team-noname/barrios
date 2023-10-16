from emmett.orm import Model, Field, belongs_to

class FlightPlanEntry(Model):
    tablename = 'iss_flight_plan'
    belongs_to('upload')

    datedim = Field.date()
    vehicle_name = Field.text()
    port_name = Field.Text()
    vehicle_type = Field.Text()
    eva_name = Field.Text()
    eva_type = Field.Text()
    eva_accuracy = Field.Text()