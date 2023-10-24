"""Remove upload relation and store flat files

Migration ID: d860e55f7a6c
Revises: d0e6fa546000
Creation Date: 2023-10-23 18:49:14.986279

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = 'd860e55f7a6c'
    revises = 'd0e6fa546000'

    def up(self):
        self.add_column('uploads', migrations.Column('file_path', 'text'))
        self.drop_column('ims_consumables_category_lookup', 'upload')
        self.drop_column('inventory_management_system_consumables', 'upload')
        self.drop_column('iss_flight_plan', 'upload')
        self.drop_column('iss_flight_plan_crew', 'upload')
        self.drop_column('iss_flight_plan_crew_nationality_lookup', 'upload')
        self.drop_column('rates_definition', 'upload')
        self.drop_column('rsa_consumable_water_summary', 'upload')
        self.drop_column('stored_items_only_inventory_mgmt_system_consumables', 'upload')
        self.drop_column('tank_capacity_definition', 'upload')
        self.drop_column('thresholds_limits_definition', 'upload')
        self.drop_column('us_rs_weekly_consumable_gas_summary', 'upload')
        self.drop_column('us_weekly_consumable_water_summary', 'upload')

    def down(self):
        self.add_column('us_weekly_consumable_water_summary', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('us_rs_weekly_consumable_gas_summary', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('thresholds_limits_definition', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('tank_capacity_definition', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('stored_items_only_inventory_mgmt_system_consumables', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('rsa_consumable_water_summary', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('rates_definition', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('iss_flight_plan_crew_nationality_lookup', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('iss_flight_plan_crew', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('iss_flight_plan', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('inventory_management_system_consumables', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.add_column('ims_consumables_category_lookup', migrations.Column('upload', 'reference uploads', ondelete='CASCADE'))
        self.drop_column('uploads', 'file_path')
