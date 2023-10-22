"""Setup user data tables

Migration ID: 267d1f58a6c5
Revises: 9869b609f1ad
Creation Date: 2023-10-21 21:05:28.743028

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '267d1f58a6c5'
    revises = '9869b609f1ad'

    def up(self):
        self.create_table(
            'ims_consumables_category_lookup_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('category_name', 'text'),
            migrations.Column('categoryID', 'integer'),
            migrations.Column('module_name', 'text'),
            migrations.Column('moduleID', 'integer'),
            migrations.Column('unique_cat_mod_ID', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'inventory_mgmt_system_consumables_entrys',
            migrations.Column('datedim', 'text'),
            migrations.Column('id', 'integer'),
            migrations.Column('id_parent', 'integer'),
            migrations.Column('id_path', 'text'),
            migrations.Column('tree_depth', 'integer'),
            migrations.Column('tree', 'text'),
            migrations.Column('part_number', 'text'),
            migrations.Column('serial_number', 'integer'),
            migrations.Column('location_name', 'text'),
            migrations.Column('original_ip_owner', 'text'),
            migrations.Column('current_ip_owner', 'text'),
            migrations.Column('operational_nomenclature', 'text'),
            migrations.Column('russian_name', 'text'),
            migrations.Column('english_name', 'text'),
            migrations.Column('barcode', 'text'),
            migrations.Column('quantity', 'integer'),
            migrations.Column('width', 'float'),
            migrations.Column('height', 'float'),
            migrations.Column('length', 'float'),
            migrations.Column('diameter', 'float'),
            migrations.Column('calculated_volume', 'float'),
            migrations.Column('stwg_ovrrd_vol', 'float'),
            migrations.Column('children_volume', 'float'),
            migrations.Column('stwg_ovrrd_chldrn_vol', 'float'),
            migrations.Column('ovrrd_notes', 'text'),
            migrations.Column('volume_notes', 'text'),
            migrations.Column('expire_date', 'text'),
            migrations.Column('launch', 'text'),
            migrations.Column('type', 'text'),
            migrations.Column('hazard', 'text'),
            migrations.Column('state', 'text'),
            migrations.Column('status', 'text'),
            migrations.Column('is_container', 'integer'),
            migrations.Column('is_moveable', 'integer'),
            migrations.Column('system', 'text'),
            migrations.Column('subsystem', 'text'),
            migrations.Column('action_date', 'text'),
            migrations.Column('move_date', 'text'),
            migrations.Column('fill_status', 'text'),
            migrations.Column('categoryID', 'text'),
            migrations.Column('category_name', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'iss_flight_plan_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('datedim', 'text'),
            migrations.Column('vehicle_name', 'text'),
            migrations.Column('port_name', 'text'),
            migrations.Column('vehicle_type', 'text'),
            migrations.Column('eva_name', 'text'),
            migrations.Column('eva_type', 'text'),
            migrations.Column('eva_accuracy', 'text'),
            migrations.Column('event', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'iss_flight_plan_crew_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('datedim', 'text'),
            migrations.Column('nationality_category', 'text'),
            migrations.Column('crew_count', 'integer'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'iss_flight_plan_crew_nationality_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('nationality', 'text'),
            migrations.Column('is_usos_crew', 'integer'),
            migrations.Column('is_rsa_crew', 'integer'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'rates_definition_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('rate_category', 'text'),
            migrations.Column('affected_consumable', 'text'),
            migrations.Column('rate', 'float'),
            migrations.Column('units', 'text'),
            migrations.Column('type', 'text'),
            migrations.Column('efficiency', 'integer'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'rsa_consumable_water_summary_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('report_date', 'text'),
            migrations.Column('remain_potable_liters', 'float'),
            migrations.Column('remain_technical_liters', 'float'),
            migrations.Column('remain_rodnik_liters', 'float'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'stored_items_only_inventory_mgmt_system_consumables_entrys',
            migrations.Column('datedim', 'text'),
            migrations.Column('id', 'integer'),
            migrations.Column('id_parent', 'integer'),
            migrations.Column('id_path', 'text'),
            migrations.Column('tree_depth', 'integer'),
            migrations.Column('tree', 'text'),
            migrations.Column('part_number', 'text'),
            migrations.Column('serial_number', 'integer'),
            migrations.Column('location_name', 'text'),
            migrations.Column('original_ip_owner', 'text'),
            migrations.Column('current_ip_owner', 'text'),
            migrations.Column('operational_nomenclature', 'text'),
            migrations.Column('russian_name', 'text'),
            migrations.Column('english_name', 'text'),
            migrations.Column('barcode', 'text'),
            migrations.Column('quantity', 'integer'),
            migrations.Column('width', 'float'),
            migrations.Column('height', 'float'),
            migrations.Column('length', 'float'),
            migrations.Column('diameter', 'float'),
            migrations.Column('calculated_volume', 'float'),
            migrations.Column('stwg_ovrrd_vol', 'float'),
            migrations.Column('children_volume', 'float'),
            migrations.Column('stwg_ovrrd_chldrn_vol', 'float'),
            migrations.Column('ovrrd_notes', 'text'),
            migrations.Column('volume_notes', 'text'),
            migrations.Column('expire_date', 'text'),
            migrations.Column('launch', 'text'),
            migrations.Column('type', 'text'),
            migrations.Column('hazard', 'text'),
            migrations.Column('state', 'text'),
            migrations.Column('status', 'text'),
            migrations.Column('is_container', 'integer'),
            migrations.Column('is_moveable', 'integer'),
            migrations.Column('system', 'text'),
            migrations.Column('subsystem', 'text'),
            migrations.Column('action_date', 'text'),
            migrations.Column('move_date', 'text'),
            migrations.Column('fill_status', 'text'),
            migrations.Column('categoryID', 'text'),
            migrations.Column('category_name', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'tank_capacity_definition_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('tank_category', 'text'),
            migrations.Column('tank_capacity', 'float'),
            migrations.Column('units', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'thresholds_limits_definition_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('threshold_category', 'text'),
            migrations.Column('threshold_value', 'float'),
            migrations.Column('threshold_owner', 'text'),
            migrations.Column('units', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'us_rs_weekly_consumable_gas_summary_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('date', 'text'),
            migrations.Column('usos_o2_kg', 'float'),
            migrations.Column('rs_o2_kg', 'float'),
            migrations.Column('rs_n2_kg', 'float'),
            migrations.Column('Adjusted_o2_kg', 'float'),
            migrations.Column('Adjusted_n2_kg', 'float'),
            migrations.Column('Resupply_o2_kg', 'float'),
            migrations.Column('Resupply_n2_kg', 'float'),
            migrations.Column('resupply_air_kg', 'float'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'us_weekly_consumable_water_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('date', 'date'),
            migrations.Column('corrected_potable_l', 'float'),
            migrations.Column('corrected_technical_l', 'float'),
            migrations.Column('corrected_total_l', 'float'),
            migrations.Column('resupply_potable_l', 'float'),
            migrations.Column('resupply_technical_l', 'float'),
            migrations.Column('corrected_predicted_l', 'float'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.drop_table('flight_plan_crew_entrys')
        self.drop_table('flight_plan_entrys')
        self.drop_table('gas_entrys')
        self.drop_table('water_entrys')

    def down(self):
        self.create_table(
            'water_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('date', 'date'),
            migrations.Column('corrected_potable_l', 'float'),
            migrations.Column('corrected_technical_l', 'float'),
            migrations.Column('corrected_total_l', 'float'),
            migrations.Column('resupply_potable_l', 'float'),
            migrations.Column('resupply_technical_l', 'float'),
            migrations.Column('corrected_predicted_l', 'float'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'gas_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('date', 'date'),
            migrations.Column('usos_o2_kg', 'float'),
            migrations.Column('rs_o2_kg', 'float'),
            migrations.Column('us_n2_kg', 'float'),
            migrations.Column('rs_n2_kg', 'float'),
            migrations.Column('adjusted_o2_kg', 'float'),
            migrations.Column('adjusted_n2_kg', 'float'),
            migrations.Column('resupply_o2_kg', 'float'),
            migrations.Column('resupply_n2_kg', 'float'),
            migrations.Column('resupply_air_kg', 'float'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'flight_plan_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('datedim', 'date'),
            migrations.Column('vehicle_name', 'text'),
            migrations.Column('port_name', 'text'),
            migrations.Column('vehicle_type', 'text'),
            migrations.Column('eva_name', 'text'),
            migrations.Column('eva_type', 'text'),
            migrations.Column('eva_accuracy', 'text'),
            migrations.Column('event', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'flight_plan_crew_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('datedim', 'date'),
            migrations.Column('nationality_category', 'text'),
            migrations.Column('crew_count', 'integer'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.drop_table('us_weekly_consumable_water_entrys')
        self.drop_table('us_rs_weekly_consumable_gas_summary_entrys')
        self.drop_table('thresholds_limits_definition_entrys')
        self.drop_table('tank_capacity_definition_entrys')
        self.drop_table('stored_items_only_inventory_mgmt_system_consumables_entrys')
        self.drop_table('rsa_consumable_water_summary_entrys')
        self.drop_table('rates_definition_entrys')
        self.drop_table('iss_flight_plan_crew_nationality_entrys')
        self.drop_table('iss_flight_plan_crew_entrys')
        self.drop_table('iss_flight_plan_entrys')
        self.drop_table('inventory_mgmt_system_consumables_entrys')
        self.drop_table('ims_consumables_category_lookup_entrys')
