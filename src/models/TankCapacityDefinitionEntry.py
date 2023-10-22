from emmett.orm import Model, Field, belongs_to

class TankCapacityDefinitionEntry(Model):
    tablename = 'tank_capacity_definition'
    belongs_to('upload')
    tank_category = Field.text()
    tank_capacity = Field.float()
    units = Field.text()

    validation = {
        'tank_category': {'presence': True},
        'tank_capacity': {'presence': True},
        'units': {'presence': True}
    }