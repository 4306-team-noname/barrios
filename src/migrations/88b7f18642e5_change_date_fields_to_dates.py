"""Change date fields to dates

Migration ID: 88b7f18642e5
Revises: 
Creation Date: 2023-10-22 17:01:49.072798

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '88b7f18642e5'
    revises = None

    def up(self):
        self.create_table(
            'users',
            migrations.Column('id', 'id'),
            migrations.Column('created_at', 'datetime'),
            migrations.Column('updated_at', 'datetime'),
            migrations.Column('email', 'string', length=255),
            migrations.Column('password', 'password', length=512),
            migrations.Column('registration_key', 'string', default='', length=512),
            migrations.Column('reset_password_key', 'string', default='', length=512),
            migrations.Column('registration_id', 'string', default='', length=512),
            migrations.Column('first_name', 'string', notnull=True, length=128),
            migrations.Column('last_name', 'string', notnull=True, length=128),
            primary_keys=['id'])
        self.create_index('users_widx__email_unique', 'users', ['email'], expressions=[], unique=True)
        self.create_table(
            'auth_groups',
            migrations.Column('id', 'id'),
            migrations.Column('created_at', 'datetime'),
            migrations.Column('updated_at', 'datetime'),
            migrations.Column('role', 'string', default='', length=255),
            migrations.Column('description', 'text'),
            primary_keys=['id'])
        self.create_index('auth_groups_widx__role_unique', 'auth_groups', ['role'], expressions=[], unique=True)
        self.create_table(
            'auth_memberships',
            migrations.Column('id', 'id'),
            migrations.Column('created_at', 'datetime'),
            migrations.Column('updated_at', 'datetime'),
            migrations.Column('user', 'reference users', ondelete='CASCADE'),
            migrations.Column('auth_group', 'reference auth_groups', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'auth_permissions',
            migrations.Column('id', 'id'),
            migrations.Column('created_at', 'datetime'),
            migrations.Column('updated_at', 'datetime'),
            migrations.Column('name', 'string', default='default', notnull=True, length=512),
            migrations.Column('table_name', 'string', length=512),
            migrations.Column('record_id', 'integer', default=0),
            migrations.Column('auth_group', 'reference auth_groups', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'auth_events',
            migrations.Column('id', 'id'),
            migrations.Column('created_at', 'datetime'),
            migrations.Column('updated_at', 'datetime'),
            migrations.Column('client_ip', 'string', length=512),
            migrations.Column('origin', 'string', default='auth', notnull=True, length=512),
            migrations.Column('description', 'text', default='', notnull=True),
            migrations.Column('user', 'reference users', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'uploads',
            migrations.Column('id', 'id'),
            migrations.Column('file_name', 'text'),
            migrations.Column('upload_date', 'datetime'),
            primary_keys=['id'])
        self.create_index('uploads_widx__file_name_unique', 'uploads', ['file_name'], expressions=[], unique=True)
        self.create_table(
            'ims_consumables_category_lookup',
            migrations.Column('category_name', 'text'),
            migrations.Column('categoryID', 'integer'),
            migrations.Column('module_name', 'text'),
            migrations.Column('moduleID', 'integer'),
            migrations.Column('unique_cat_mod_ID', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['categoryID'])
        self.create_table(
            'inventory_management_system_consumables',
            migrations.Column('datedim', 'date'),
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
            'iss_flight_plan',
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
        self.create_index('iss_flight_plan_widx__datedim_unique', 'iss_flight_plan', ['datedim'], expressions=[], unique=True)
        self.create_table(
            'iss_flight_plan_crew',
            migrations.Column('id', 'id'),
            migrations.Column('datedim', 'date'),
            migrations.Column('nationality_category', 'text'),
            migrations.Column('crew_count', 'integer'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_index('iss_flight_plan_crew_widx__datedim_unique', 'iss_flight_plan_crew', ['datedim'], expressions=[], unique=True)
        self.create_table(
            'iss_flight_plan_crew_nationality_lookup',
            migrations.Column('id', 'id'),
            migrations.Column('nationality', 'text'),
            migrations.Column('is_usos_crew', 'integer'),
            migrations.Column('is_rsa_crew', 'integer'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_index('iss_flight_plan_crew_nationality_lookup_widx__nationality_unique', 'iss_flight_plan_crew_nationality_lookup', ['nationality'], expressions=[], unique=True)
        self.create_table(
            'rates_definition',
            migrations.Column('id', 'id'),
            migrations.Column('rate_category', 'text'),
            migrations.Column('affected_consumable', 'text'),
            migrations.Column('rate', 'float'),
            migrations.Column('units', 'text'),
            migrations.Column('type', 'text'),
            migrations.Column('efficiency', 'integer'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_index('rates_definition_widx__rate_category_unique', 'rates_definition', ['rate_category'], expressions=[], unique=True)
        self.create_table(
            'rsa_consumable_water_summary',
            migrations.Column('id', 'id'),
            migrations.Column('report_date', 'date'),
            migrations.Column('remain_potable_liters', 'float'),
            migrations.Column('remain_technical_liters', 'float'),
            migrations.Column('remain_rodnik_liters', 'float'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_index('rsa_consumable_water_summary_widx__report_date_unique', 'rsa_consumable_water_summary', ['report_date'], expressions=[], unique=True)
        self.create_table(
            'stored_items_only_inventory_mgmt_system_consumables',
            migrations.Column('datedim', 'date'),
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
            'tank_capacity_definition',
            migrations.Column('id', 'id'),
            migrations.Column('tank_category', 'text'),
            migrations.Column('tank_capacity', 'float'),
            migrations.Column('units', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_index('tank_capacity_definition_widx__tank_category_unique', 'tank_capacity_definition', ['tank_category'], expressions=[], unique=True)
        self.create_table(
            'thresholds_limits_definition',
            migrations.Column('id', 'id'),
            migrations.Column('threshold_category', 'text'),
            migrations.Column('threshold_value', 'float'),
            migrations.Column('threshold_owner', 'text'),
            migrations.Column('units', 'text'),
            migrations.Column('upload', 'reference uploads', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_index('thresholds_limits_definition_widx__threshold_category_unique', 'thresholds_limits_definition', ['threshold_category'], expressions=[], unique=True)
        self.create_table(
            'us_rs_weekly_consumable_gas_summary',
            migrations.Column('id', 'id'),
            migrations.Column('date', 'date'),
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
        self.create_index('us_rs_weekly_consumable_gas_summary_widx__date_unique', 'us_rs_weekly_consumable_gas_summary', ['date'], expressions=[], unique=True)
        self.create_table(
            'us_weekly_consumable_water_summary',
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
        self.create_index('us_weekly_consumable_water_summary_widx__date_unique', 'us_weekly_consumable_water_summary', ['date'], expressions=[], unique=True)

    def down(self):
        self.drop_index('us_weekly_consumable_water_summary_widx__date_unique', 'us_weekly_consumable_water_summary')
        self.drop_table('us_weekly_consumable_water_summary')
        self.drop_index('us_rs_weekly_consumable_gas_summary_widx__date_unique', 'us_rs_weekly_consumable_gas_summary')
        self.drop_table('us_rs_weekly_consumable_gas_summary')
        self.drop_index('thresholds_limits_definition_widx__threshold_category_unique', 'thresholds_limits_definition')
        self.drop_table('thresholds_limits_definition')
        self.drop_index('tank_capacity_definition_widx__tank_category_unique', 'tank_capacity_definition')
        self.drop_table('tank_capacity_definition')
        self.drop_table('stored_items_only_inventory_mgmt_system_consumables')
        self.drop_index('rsa_consumable_water_summary_widx__report_date_unique', 'rsa_consumable_water_summary')
        self.drop_table('rsa_consumable_water_summary')
        self.drop_index('rates_definition_widx__rate_category_unique', 'rates_definition')
        self.drop_table('rates_definition')
        self.drop_index('iss_flight_plan_crew_nationality_lookup_widx__nationality_unique', 'iss_flight_plan_crew_nationality_lookup')
        self.drop_table('iss_flight_plan_crew_nationality_lookup')
        self.drop_index('iss_flight_plan_crew_widx__datedim_unique', 'iss_flight_plan_crew')
        self.drop_table('iss_flight_plan_crew')
        self.drop_index('iss_flight_plan_widx__datedim_unique', 'iss_flight_plan')
        self.drop_table('iss_flight_plan')
        self.drop_table('inventory_management_system_consumables')
        self.drop_table('ims_consumables_category_lookup')
        self.drop_index('uploads_widx__file_name_unique', 'uploads')
        self.drop_table('uploads')
        self.drop_table('auth_events')
        self.drop_table('auth_permissions')
        self.drop_table('auth_memberships')
        self.drop_index('auth_groups_widx__role_unique', 'auth_groups')
        self.drop_table('auth_groups')
        self.drop_index('users_widx__email_unique', 'users')
        self.drop_table('users')
