from datetime import date
from data.models import IssFlightPlan


def get_flightplan_dates(event_type=None) -> list[date]:
    """
    Get a list of dates that have flight plan events.
    Params:
        event_type : str
            The event type to filter on. If None, return all dates.
            valid event types: None, "Launch", "Dock", "Undock", "Landing", "EVA"
    """
    if event_type is None:
        fp_qs = IssFlightPlan.objects.all().values("datedim")
        fp_dates = [d["datedim"] for d in fp_qs]
        return fp_dates
    else:
        fp_qs = IssFlightPlan.objects.filter(event=event_type).values("datedim")
        fp_dates = [d["datedim"] for d in fp_qs]
        return fp_dates


def get_flightplan_deltas(date_list: list[date]) -> list[int]:
    """
    Get a list of deltas between dates.
    Params:
        date_list : list[date]
            A list of dates to get deltas between
    """
    days_list = []
    for idx, d1 in enumerate(date_list):
        j = idx + 1
        if j < len(date_list):
            d2 = date_list[j]
            delta = d2 - d1
            days_list.append(delta.days)
    return days_list
