"""Define gas and water models

Migration ID: 9869b609f1ad
Revises: a97f5ffdc6d4
Creation Date: 2023-10-17 09:11:52.944841

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '9869b609f1ad'
    revises = 'a97f5ffdc6d4'

    def up(self):
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

    def down(self):
        self.drop_table('water_entrys')
        self.drop_table('gas_entrys')
