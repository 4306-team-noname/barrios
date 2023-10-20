"""First migration

Migration ID: 17cd958d56a2
Revises: 8335de8332d9
Creation Date: 2023-10-17 08:31:14.244835

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '17cd958d56a2'
    revises = '8335de8332d9'

    def up(self):
        self.create_table(
            'uploads',
            migrations.Column('id', 'id'),
            migrations.Column('file_name', 'text'),
            migrations.Column('upload_date', 'datetime'),
            migrations.Column('user', 'reference users', ondelete='CASCADE'),
            primary_keys=['id'])
        self.create_table(
            'flight_plan_crew_entrys',
            migrations.Column('id', 'id'),
            migrations.Column('datedim', 'date'),
            migrations.Column('nationality_category', 'text'),
            migrations.Column('crew_count', 'integer'),
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

    def down(self):
        self.drop_table('flight_plan_entrys')
        self.drop_table('flight_plan_crew_entrys')
        self.drop_table('uploads')
