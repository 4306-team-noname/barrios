"""Add unique constraint to upload filename

Migration ID: 8f31a0400631
Revises: 2490953ae9ef
Creation Date: 2023-10-22 09:20:54.933196

"""

from emmett.orm import migrations


class Migration(migrations.Migration):
    revision = '8f31a0400631'
    revises = '2490953ae9ef'

    def up(self):
        self.create_index('uploads_widx__file_name_unique', 'uploads', ['file_name'], expressions=[], unique=True)

    def down(self):
        self.drop_index('uploads_widx__file_name_unique', 'uploads')
