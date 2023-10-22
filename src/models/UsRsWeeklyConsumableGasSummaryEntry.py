from emmett.orm import Model, Field, belongs_to

class UsRsWeeklyConsumableGasSummaryEntry(Model):
    tablename = 'us_rs_weekly_consumable_gas_summary'
    belongs_to('upload')
    date = Field.date(unique=True)
    usos_o2_kg = Field.float()
    rs_o2_kg = Field.float()
    rs_n2_kg = Field.float()
    rs_n2_kg = Field.float()
    Adjusted_o2_kg = Field.float()
    Adjusted_n2_kg = Field.float()
    Resupply_o2_kg = Field.float()
    Resupply_n2_kg = Field.float()
    resupply_air_kg = Field.float()



    validation = {
        'date': {'presence': True},
        'usos_o2_kg': {'presence': True},
        'rs_o2_kg': {'presence': True},
        'rs_n2_kg': {'presence': True},
        'rs_n2_kg': {'presence': True},
        'Adjusted_o2_kg': {'presence': True},
        'Adjusted_n2_kg': {'presence': True},
    }