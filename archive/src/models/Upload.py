from emmett.orm import Model, Field
from emmett import now


class Upload(Model):
    # belongs_to('user')
    file_name = Field.text(unique=True)
    file_path = Field.text()
    upload_date = Field.datetime()

    default_values = {"upload_date": now}

    validation = {
        "file_name": {"presence": True},
        "file_path": {"presence": True},
        "upload_date": {"presence": True},
    }
