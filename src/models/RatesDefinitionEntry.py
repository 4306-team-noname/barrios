from emmett.orm import Model, Field, belongs_to

class RatesDefinitionEntry(Model):
    tablename = 'rates_definition'
    belongs_to('upload')
    rate_category = Field.text(unique=True)
    affected_consumable = Field.text()
    rate = Field.float()
    units = Field.text()
    type = Field.text()
    efficiency = Field.int()

    validation = {
        'rate_category': {'presence': True, 'unique': True},
        'affected_consumable': {'presence': True},
        'rate': {'presence': True},
        'units': {'presence': True},
        'type': {'presence': True},
        'efficiency': {'allow': None}
    }