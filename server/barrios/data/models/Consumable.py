from django.db.models import CASCADE, CharField, ForeignKey, Model


class Consumable(Model):
    name = CharField(max_length=255)
    category = ForeignKey("Category", to_field="category_id", on_delete=CASCADE)

    def __repr__(self):
        return {"name": self.name, "category_id": self.category}

    class Meta:
        db_table = "consumables"
