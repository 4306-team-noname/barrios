from django.db.models import (
    RESTRICT,
    IntegerField,
    CharField,
    Manager,
    Model,
    OneToOneField,
)

from data.models import ImsModel


class ImsConsumablesCategoryLookup(ImsModel):
    category_name = CharField()
    category = OneToOneField("Category", on_delete=RESTRICT, to_field="category_id")
    module_name = CharField(max_length=255)
    module_id = IntegerField()
    unique_cat_mod_id = CharField(max_length=255, unique=True)

    # objects = EmptyKeywordManager()
    readable_name = "Category Lookup"

    class Meta:
        db_table = "ims_consumables_category_lookup"

    def __str__(self):
        return f"""\t{{
            category_id: {self.category},
            category_name: {self.category_name},
            module_id: {self.module_id},
            module_name: {self.module_name},
            "unique_cat_mod_id": {self.unique_cat_mod_id}
        }}"""
