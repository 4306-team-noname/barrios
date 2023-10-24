from emmett.orm import Model, Field
class TankCapacityDefinition(Model):
    tablename = 'tank_capacity_definition'
    
    tank_category = Field.text(unique=True)
    tank_capacity = Field.float()
    units = Field.text()

    validation = {
        'tank_category': {'presence': True},
        'tank_capacity': {'presence': True},
        'units': {'presence': True}
    }