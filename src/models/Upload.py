from emmett.orm import Model, Field, belongs_to

class Upload(Model):
    belongs_to('user')
    