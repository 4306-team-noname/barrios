"""Update efficiency field to float

Migration ID: 9d337ebaad45
Revises: d860e55f7a6c
Creation Date: 2023-10-23 20:34:02.169446

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '9d337ebaad45'
    revises = 'd860e55f7a6c'

    def up(self):
        self.alter_column('rates_definition', 'efficiency',
            existing_type='integer',
            existing_length=255,
            type='float',
            existing_notnull=False)

    def down(self):
        self.alter_column('rates_definition', 'efficiency',
            existing_type='float',
            existing_length=255,
            type='integer',
            existing_notnull=False)
