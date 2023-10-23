"""Really switch field names to snake_case

Migration ID: d49e2570f01f
Revises: 139c7d6a14a8
Creation Date: 2023-10-22 17:14:09.331867

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = 'd49e2570f01f'
    revises = '139c7d6a14a8'

    def up(self):
        self.add_column('ims_consumables_category_lookup', migrations.Column('unique_cat_mod_id', 'text', notnull=True))
        self.drop_column('ims_consumables_category_lookup', 'unique_cat_mod_ID')

    def down(self):
        self.add_column('ims_consumables_category_lookup', migrations.Column('unique_cat_mod_ID', 'text', notnull=True))
        self.drop_column('ims_consumables_category_lookup', 'unique_cat_mod_id')
