from django.http import HttpResponse
from django.shortcuts import redirect, render
from common.conditionalredirect import conditionalredirect
from forecast.create_forecast_chart import create_forecast_chart
from forecast.create_forecast import create_forecast


def index(request):
    if request.user.is_authenticated:
        return render(request, "pages/forecast/index.html")
    else:
        return conditionalredirect(request, "/accounts/login/")


def get_forecast(request, consumable_name):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    forecast_obj = create_forecast(consumable_name)
    line_plot = create_forecast_chart(forecast_obj)

    return render(
        request,
        "pages/forecast/forecast_plot.html",
        {"forecast_plot": line_plot, "current": consumable_name},
    )
