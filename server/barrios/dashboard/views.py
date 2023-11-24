from django.shortcuts import redirect, render
from random import randint
from datetime import date, datetime, timedelta
from plotly.offline import plot
import plotly.express as px
import pandas as pd


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
        forecasts = get_forecasts(request)
        df = pd.DataFrame(forecasts)
        fig = px.line(df, x="date", y=list(df.columns)[1:])
        fig.update_layout(
            paper_bgcolor="#091D41",
            plot_bgcolor="#091D41",
            title_font_color="#ffffff",
            legend_font_color="#ffffff",
        )
        line_plot = plot(fig, output_type="div")
        return render(
            request,
            "pages/dashboard/index.html",
            {
                "usage_difference": get_usage(request),
                "last_optimization": get_optimizations(request),
                "last_forecast": get_forecasts(request),
                "forecast_plot": line_plot,
            },
        )
    else:
        return redirect("/accounts/login")


def get_usage(request):
    return randint(-50, 50)


def get_optimizations(request):
    dummy_opts = {"launch_name": "SPX29", "launch_date": "12/01/2023", "payload": []}
    for consumable in DUMMY_CONSUMABLES:
        cp = {"amount": randint(1, 100), **consumable}
        dummy_opts["payload"].append(cp)
    return dummy_opts


def get_forecasts(request):
    next_launch = date(2023, 12, 23)
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
    return dummy_forecast
