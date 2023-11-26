from django.http import HttpResponse
from django.shortcuts import redirect, render
from common.conditionalredirect import conditionalredirect
from data.models import IssFlightPlan


def index(request):
    if request.user.is_authenticated:
        return render(request, "pages/forecast/index.html")
    else:
        return conditionalredirect(request, "/accounts/login")


def get_forecast(request, consumable_name):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")
    docking_date_values = IssFlightPlan.objects.filter(event="Dock").values("datedim")
    docking_dates = [d["datedim"] for d in docking_date_values]

    mission_period = timedelta(days=180)
    launch_dates = [next_launch]
    for i in range(1, 4):
        launch_dates.append(next_launch - (mission_period * i))
        launch_dates.append(next_launch + (mission_period * i))
    launch_dates.sort()
    dummy_forecast = []
    for launch_date in launch_dates:
        forecast = {
            "date": launch_date,
        }
        seedrand = randint(20, 600)
        for consumable in DUMMY_CONSUMABLES:
            forecast[consumable["name"]] = randint(seedrand - 60, seedrand + 60)
        dummy_forecast.append(forecast)
