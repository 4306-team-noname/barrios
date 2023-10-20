from emmett.orm import Model, Field, belongs_to

class GasEntry(Model):
    belongs_to('upload')
    date = Field.date()
    usos_o2_kg = Field.float()
    rs_o2_kg = Field.float()
    us_n2_kg = Field.float()
    rs_n2_kg = Field.float()
    adjusted_o2_kg = Field.float()
    adjusted_n2_kg = Field.float()
    resupply_o2_kg = Field.float()
    resupply_n2_kg = Field.float()
    resupply_air_kg = Field.float()

    validation = {
        'date': {'presence': True},
        'usos_o2_kg': {'presence': True},
        'rs_o2_kg': {'presence': True},
        'us_n2_kg': {'presence': True},
        'rs_n2_kg': {'presence': True},
        'adjusted_o2_kg': {'presence': True},
        'adjusted_n2_kg': {'presence': True},
    }
