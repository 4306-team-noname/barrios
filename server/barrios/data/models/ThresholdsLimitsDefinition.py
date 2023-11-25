from django.db.models import CASCADE, FloatField, ForeignKey, CharField
from data.models import ImsModel


class ThresholdsLimitsDefinition(ImsModel):
    # TODO: Since we're declaring a foreign key relation
    # to the category lookups table and none of the original
    # fields from the user-provided CSV files match that table
    # we're going to need a way to match the `threshold_category`
    # field with that table. We'll need a lookup table or something.
    threshold_category = CharField(max_length=255, blank=True, null=True)
    threshold_value = FloatField()
    threshold_owner = CharField(max_length=255, blank=True, null=True)
    units = CharField(max_length=255, blank=True, null=True)
    # might be best to set this as a foreign key to a separate
    # 'categories' table that we populate ourselves
    category = ForeignKey(
        "Category", to_field="category_id", on_delete=CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "thresholds_limits_definition"
