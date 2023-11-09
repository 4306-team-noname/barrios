from django.db.models import (
    RESTRICT,
    IntegerField,
    CharField,
    Model,
    OneToOneField,
)

# from .UserDataEntry import UserDataEntry


class ImsConsumablesCategoryLookup(Model):
    category_name = CharField()
    category_id = OneToOneField(
        "Category", on_delete=RESTRICT, to_field="category_id", primary_key=True
    )
    module_name = CharField(max_length=200, unique=True)
    module_id = IntegerField()
    unique_cat_mod_id = CharField(max_length=200, unique=True)

    class Meta:
        db_table = "ims_consumables_category_lookups"

    def __str__(self):
        return f"""{{
            category_id: {self.category_id},
            category_name: {self.category_name},
            module_id: {self.module_id},
            module_name: {self.module_name},
            "unique_cat_mod_id": {self.unique_cat_mod_id}
        }}"""
