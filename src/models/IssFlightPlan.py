from emmett.orm import Model, Field


class IssFlightPlan(Model):
    tablename = 'iss_flight_plan'

    datedim = Field.date(unique=True)
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

