from emmett.orm import Model, Field
class RsaConsumableWaterSummary(Model):
    tablename = 'rsa_consumable_water_summary'

    report_date = Field.date(unique=True)
    remain_potable_liters = Field.float()
    remain_technical_liters = Field.float()
    remain_rodnik_liters = Field.float()

    validation = {
        'report_date': {'presence': True},
        'remain_potable_liters': {'presence': True},
        'remain_technical_liters': {'presence': True},
        'remain_rodnik_liters': {'presence': True},
    }