from emmett.orm import Model, Field
class UsWeeklyConsumableWaterSummary(Model):
    tablename = 'us_weekly_consumable_water_summary'
    
    date = Field.date(unique=True)
    corrected_potable_l = Field.float()
    corrected_technical_l = Field.float()
    corrected_total_l = Field.float()
    resupply_potable_l = Field.float()
    resupply_technical_l = Field.float()
    corrected_predicted_l = Field.float()

    validation = {
        'date': {'presence': True},
        'corrected_potable_l': {'presence': True},
        'corrected_technical_l': {'presence': True},
        'corrected_total_l': {'presence': True},
        'corrected_predicted_l': {'presence': True},
        'resupply_potable_l': {'allow': None},
        'resupply_technical_l': {'allow': None},
        'corrected_predicted_l': {'allow': None},
    }