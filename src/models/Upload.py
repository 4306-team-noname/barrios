from emmett.orm import Model, Field, belongs_to
from emmett import session, now

class Upload(Model):
    # belongs_to('user')
    file_name = Field.text(unique=True)
    upload_date = Field.datetime()

    default_values = {
        'upload_date': now
    }

    validation = {
        'file_name': {'presence': True},
        'upload_date': {'presence': True}
    }
