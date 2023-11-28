from django.shortcuts import redirect, render
from random import randint
from datetime import date, datetime, timedelta
from plotly.offline import plot
import plotly.express as px
import pandas as pd
from common.conditionalredirect import conditionalredirect
from forecast.views import get_forecast
from forecast.create_forecast import create_forecast
from forecast.create_forecast_chart import create_forecast_chart


DUMMY_CONSUMABLES = [
    {"name": "ACY Insert", "unit": "ACY Insert"},
    {"name": "KTO", "unit": "KTO"},
    {"name": "Pretreat Tanks", "unit": "Pretreat Tanks"},
    {"name": "Filter Inserts", "unit": "Filter Inserts"},
    {"name": "Urine Receptacle", "unit": "Urine Receptacle"},
    {"name": "EDVs", "unit": "EDVs"},
    {"name": "O2", "unit": "lbs"},
    {"name": "N2", "unit": "lbs"},
    {"name": "Water", "unit": "Liters"},
]


def index(request):
    if request.user.is_authenticated:
        forecast_obj = create_forecast("ACY Insert")
        forecast_plot = create_forecast_chart(forecast_obj)

        return render(
            request,
            "pages/dashboard/index.html",
            {
                "usage_difference": get_usage(request),
                "last_optimization": get_optimizations(request),
                "forecast_plot": forecast_plot,
                "current": "ACY Insert",
                "current_page": "dashboard",
            },
        )
    else:
        return conditionalredirect(request, "/accounts/login/")


def get_usage(request):
    return randint(-50, 50)


def get_optimizations(request):
    dummy_opts = {"launch_name": "SPX29", "launch_date": "12/01/2023", "payload": []}
    for consumable in DUMMY_CONSUMABLES:
        cp = {"amount": randint(1, 100), **consumable}
        dummy_opts["payload"].append(cp)
    return dummy_opts
