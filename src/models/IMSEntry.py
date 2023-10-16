from emmett.orm import Model, Field, belongs_to

class IMSEntry(Model):
    belongs_to('upload')