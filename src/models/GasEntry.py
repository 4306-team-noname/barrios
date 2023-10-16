from emmett.orm import Model, Field, belongs_to

class GasEntry(Model):
    belongs_to('upload')