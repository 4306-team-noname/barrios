from datetime import date, datetime, timedelta
from django.shortcuts import redirect, render
from data.models import IssFlightPlan


def index(request):
    if request.user.is_authenticated:
        get_optimization(request, "US Food BOBs")
        return render(request, "pages/optimization/index.html")
    else:
        return redirect("/accounts/login")


def get_optimization(request, consumable):
    # The following call to IssFlightPlan.objects.filter()
    # is equivalent to:
    # SELECT datedim FROM iss_flight_plan WHERE event = 'Dock';
    docking_date_values = IssFlightPlan.objects.filter(event="Dock").values("datedim")

    # The above query returns a list of dicts that looks like
    # {'datedim': datetime.date(2022, 2, 17)}, so we can use
    # list comprehension to reduce that to a list of
    # datetime objects.
    docking_dates = [d["datedim"] for d in docking_date_values]
    print(f"{len(docking_dates)} docking_dates found: {docking_dates}")

    # Sweet, we have a list of date objects. Let's use that
    # to get a list of the number of days between
    # docking dates. (I extracted that logic into its
    # own function -- below this function.)
    deltas_list = get_flightplan_deltas(docking_dates)
    print(f"deltas_list: {deltas_list}")
    # ideally, we'd check whether we have any errors
    # here and either raise an exception or render a template
    # For now, let's just pass.
    pass


def get_flightplan_deltas(date_list: list[date]) -> list[int]:
    days_list = []
    for idx, d1 in enumerate(date_list):
        j = idx + 1
        if j < len(date_list):
            d2 = date_list[j]
            delta = d2 - d1
            days_list.append(delta.days)
    return days_list
