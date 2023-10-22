from emmett.orm import Model, Field, belongs_to

class ThresholdsLimitsDefinitionEntry(Model):
    tablename = 'thresholds_limits_definition'
    belongs_to('upload')
    threshold_category = Field.text(unique=True)
    threshold_value = Field.float()
    threshold_owner = Field.text()
    units = Field.text()

    validation = {
        'threshold_category': {'presence': True},
        'threshold_value': {'presence': True},
        'units': {'presence': True}
    }