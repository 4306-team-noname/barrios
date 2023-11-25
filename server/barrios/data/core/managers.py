from postgres_copy import CopyManager
from datetime import datetime


class EmptyKeywordManager(CopyManager):
    def create(self, *args, **kwargs):
        newargs = {}
        for key in kwargs.keys():
            if len(key) > 0:
                newargs[key] = kwargs[key]

        super().create(*args, **newargs)


class FlightPlanManager(EmptyKeywordManager):
    def create(self, *args, **kwargs):
        newargs = {}
        for key in kwargs.keys():
            if key == "datedim":
                if len(kwargs[key]) > 0:
                    newargs[key] = datetime.strptime(kwargs[key], "%m/%d/%Y").date()
                else:
                    newargs[key] = None
            else:
                newargs[key] = kwargs[key]
        super().create(*args, **newargs)
