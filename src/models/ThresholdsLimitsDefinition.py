from emmett.orm import Model, Field
class ThresholdsLimitsDefinition(Model):
    tablename = 'thresholds_limits_definition'

    threshold_category = Field.text(unique=True)
    threshold_value = Field.float()
    threshold_owner = Field.text()
    units = Field.text()

    validation = {
        'threshold_category': {'presence': True},
        'threshold_value': {'presence': True},
        'units': {'presence': True}
    }