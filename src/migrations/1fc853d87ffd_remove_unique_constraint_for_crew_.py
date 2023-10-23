"""Remove unique constraint for crew flight plan

Migration ID: 1fc853d87ffd
Revises: d49e2570f01f
Creation Date: 2023-10-22 18:12:45.760743

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '1fc853d87ffd'
    revises = 'd49e2570f01f'

    def up(self):
        self.drop_index('iss_flight_plan_crew_widx__datedim_unique', 'iss_flight_plan_crew')

    def down(self):
        self.create_index('iss_flight_plan_crew_widx__datedim_unique', 'iss_flight_plan_crew', ['datedim'], expressions=[], unique=True)
