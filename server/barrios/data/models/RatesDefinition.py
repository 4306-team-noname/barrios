from django.db.models import FloatField, CharField, Model, OneToOneField, RESTRICT
from data.models import ImsModel


class RatesDefinition(ImsModel):
    rate_category = CharField(max_length=255, unique=True)
    affected_consumable = CharField(max_length=255, null=True, blank=True)
    rate = FloatField()
    units = CharField(max_length=255, null=True, blank=True)
    type = CharField(max_length=255, null=True, blank=True)
    efficiency = CharField(max_length=255, null=True, blank=True)
    category = OneToOneField(
        "Category", on_delete=RESTRICT, to_field="category_id", null=True, blank=True
    )

    class Meta:
        db_table = "rates_definition"
