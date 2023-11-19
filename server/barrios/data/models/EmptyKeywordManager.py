from django.db.models import Manager


class EmptyKeywordManager(Manager):
    def create(self, *args, **kwargs):
        newargs = {}
        for key in kwargs.keys():
            if len(key) > 0:
                newargs[key] = kwargs[key]

        super().create(*args, **newargs)
