from emmett.orm import Model, belongs_to

class Entry(Model):
    belongs_to('upload')

    validation = {
        'upload': {'presence': True}
    }