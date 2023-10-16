from emmett.orm import Model, Field, belongs_to
from models.Entry import Entry
class FlightPlanEntry(Entry):
    datedim = Field.date()
    vehicle_name = Field.text()
    port_name = Field.text()
    vehicle_type = Field.text()
    eva_name = Field.text()
    eva_type = Field.text()
    eva_accuracy = Field.text()
    field_names = [
        'datedim',
        'vehicle_name',
        'port_name',
        'vehicle_type',
        'eva_name', 
        'eva_type',
        'eva_accuracy'
    ]