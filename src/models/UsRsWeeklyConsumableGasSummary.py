from emmett.orm import Model, Field

class UsRsWeeklyConsumableGasSummary(Model):
    tablename = 'us_rs_weekly_consumable_gas_summary'

    date = Field.date(unique=True)
    usos_o2_kg = Field.float()
    rs_o2_kg = Field.float()
    rs_n2_kg = Field.float()
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
        'rs_n2_kg': {'presence': True},
        'rs_n2_kg': {'presence': True},
        'adjusted_o2_kg': {'presence': True},
        'adjusted_n2_kg': {'presence': True},
        'resupply_o2_kg': {'allow': None},
        'resupply_n2_kg': {'allow': None},
        'resupply_air_kg': {'allow': None},
    }