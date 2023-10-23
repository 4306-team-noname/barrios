"""Switch field names to snake_case

Migration ID: 139c7d6a14a8
Revises: 88b7f18642e5
Creation Date: 2023-10-22 17:11:29.849452

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '139c7d6a14a8'
    revises = '88b7f18642e5'

    def up(self):
        self.add_column('ims_consumables_category_lookup', migrations.Column('category_id', 'integer', notnull=True))
        self.add_column('ims_consumables_category_lookup', migrations.Column('module_id', 'integer', notnull=True))
        self.alter_column('ims_consumables_category_lookup', 'category_name',
            existing_type='text',
            existing_length=255,
            notnull=True)
        self.alter_column('ims_consumables_category_lookup', 'module_name',
            existing_type='text',
            existing_length=255,
            notnull=True)
        self.alter_column('ims_consumables_category_lookup', 'unique_cat_mod_ID',
            existing_type='text',
            existing_length=255,
            notnull=True)
        self.drop_column('ims_consumables_category_lookup', 'categoryID')
        self.drop_column('ims_consumables_category_lookup', 'moduleID')
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('adjusted_o2_kg', 'float'))
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('adjusted_n2_kg', 'float'))
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('resupply_o2_kg', 'float'))
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('resupply_n2_kg', 'float'))
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'Adjusted_o2_kg')
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'Adjusted_n2_kg')
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'Resupply_o2_kg')
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'Resupply_n2_kg')

    def down(self):
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('Resupply_n2_kg', 'float'))
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('Resupply_o2_kg', 'float'))
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('Adjusted_n2_kg', 'float'))
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('Adjusted_o2_kg', 'float'))
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'resupply_n2_kg')
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'resupply_o2_kg')
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'adjusted_n2_kg')
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'adjusted_o2_kg')
        self.add_column('ims_consumables_category_lookup', migrations.Column('moduleID', 'integer'))
        self.add_column('ims_consumables_category_lookup', migrations.Column('categoryID', 'integer'))
        self.alter_column('ims_consumables_category_lookup', 'unique_cat_mod_ID',
            existing_type='text',
            existing_length=255,
            notnull=False)
        self.alter_column('ims_consumables_category_lookup', 'module_name',
            existing_type='text',
            existing_length=255,
            notnull=False)
        self.alter_column('ims_consumables_category_lookup', 'category_name',
            existing_type='text',
            existing_length=255,
            notnull=False)
        self.drop_column('ims_consumables_category_lookup', 'module_id')
        self.drop_column('ims_consumables_category_lookup', 'category_id')
