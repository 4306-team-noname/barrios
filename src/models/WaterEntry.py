from emmett.orm import Model, Field, belongs_to

class WaterEntry(Model):
    belongs_to('upload')
    #fields