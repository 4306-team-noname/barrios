from django.db.models import CASCADE, CharField, FloatField, ForeignKey, Model


class Consumable(Model):
    name = CharField(max_length=255)
    category = ForeignKey("Category", to_field="category_id", on_delete=CASCADE)
    assumed_rate = FloatField(blank=True, null=True)
    actual_rate = FloatField(blank=True, null=True)

    def __repr__(self):
        return {"name": self.name, "category_id": self.category}

    class Meta:
        db_table = "consumables"
