# from .UserDataEntry import UserDataEntry
from django.db.models import CASCADE, FloatField, ForeignKey, CharField, Model


class ThresholdLimitsDefinition(Model):
    # TODO: Since we're declaring a foreign key relation
    # to the category lookups table and none of the original
    # fields from the user-provided CSV files match that table
    # we're going to need a way to match the `threshold_category`
    # field with that table. We'll need a lookup table or something.
    threshold_category = CharField(unique=True, max_length=200)
    threshold_value = FloatField()
    threshold_owner = CharField(max_length=200, blank=True)
    # might be best to set this as a foreign key to a separate
    # 'categories' table that we populate ourselves
    category = ForeignKey("ImsConsumablesCategoryLookup", on_delete=CASCADE)

    class Meta:
        db_table = "thresholds_limits_definitions"
