from emmett.orm import Model
from emmett.orm import Field
from emmett.orm import belongs_to

class ImsConsumablesCategoryLookupEntry(Model):
    tablename = 'ims_consumables_category_lookup'
    primary_keys = ['categoryID']
    
    belongs_to('upload')
    category_name = Field.text()
    categoryID = Field.int()
    module_name = Field.text()
    moduleID = Field.int()
    unique_cat_mod_ID = Field.text()

    validation = {
        'category_name': {'presence': True},
        'categoryID': {'presence': True},
        'module_name': {'presence': True},
        'moduleID': {'presence': True},
        'unique_cat_mod_ID': {'presence': True},
    }