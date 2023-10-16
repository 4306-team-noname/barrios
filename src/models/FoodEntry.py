from emmett.orm import Model, Field, belongs_to

class FoodEntry(Model):
    belongs_to('upload')