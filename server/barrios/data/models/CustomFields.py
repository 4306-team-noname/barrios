from django.db.models import FloatField, IntegerField


class EmptyStringToNoneFloatField(FloatField):
    def get_prep_value(self, value):
        if value == "":
            return None
        return value


class EmptyStringToNoneIntegerField(IntegerField):
    def get_prep_value(self, value):
        if value == "":
            return None
        return value
