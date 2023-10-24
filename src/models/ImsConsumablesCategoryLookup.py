from emmett.orm import Model, Field


class ImsConsumablesCategoryLookup(Model):
    tablename = 'ims_consumables_category_lookup'
    primary_keys = ['category_id']

    category_name = Field.text(notnull=True)
    category_id = Field.int(notnull=True)
    module_name = Field.text(notnull=True)
    module_id = Field.int(notnull=True)
    unique_cat_mod_id = Field.text(notnull=True)

    validation = {
        'category_name': {'presence': True},
        'category_id': {'presence': True},
        'module_name': {'presence': True},
        'module_id': {'presence': True},
        'unique_cat_mod_id': {'presence': True},
    }

