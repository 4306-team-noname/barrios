from emmett.orm import Model, Field, belongs_to
from emmett import request

class Upload(Model):
    belongs_to('user')
    file_name = Field.text()
    upload_date = Field.datetime()

    default_values = {
        'upload_date': lambda: request.now
    }
