from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from common.conditionalredirect import conditionalredirect
from data.models.ThresholdsLimitsDefinition import ThresholdsLimitsDefinition
from forecast.create_forecast_chart import create_forecast_chart
from forecast.create_forecast import create_forecast
from common.forms import AnalysisForm


def index(request):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    form = AnalysisForm()
    return render(request, "pages/forecast/index.html", {"form": form})


def get_forecast(request, consumable_name):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    forecast_obj = create_forecast(consumable_name)
    line_plot = create_forecast_chart(forecast_obj)

    return render(
        request,
        "components/forecast_plot.html",
        {
            "forecast_plot": line_plot,
            "current": consumable_name,
        },
    )


def get_all_forecasts(request):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")


def analyze(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AnalysisForm(request.POST)
            if form.is_valid():
                start_date = form.cleaned_data["start_date"]
                end_date = form.cleaned_data["end_date"]
                consumable_name = form.cleaned_data["consumable_name"]
                return render(
                    request,
                    "pages/forecast/forecast_result.html",
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                        "consumable_name": consumable_name,
                    },
                )
            else:
                return HttpResponse()
        else:
            return conditionalredirect(request, "/forecast/")
