from emmett.orm import Model, Field, belongs_to

class WaterEntry(Model):
    belongs_to('upload')
    date = Field.date()
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
    }