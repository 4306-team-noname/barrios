from django.http import HttpResponse
from django.shortcuts import redirect, render
from common.conditionalredirect import conditionalredirect
from forecast.get_forecast_chart import get_forecast_chart


def index(request):
    if request.user.is_authenticated:
        return render(request, "pages/forecast/index.html")
    else:
        return conditionalredirect(request, "/accounts/login/")


def get_forecast(request, consumable_name):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    line_plot = get_forecast_chart(consumable_name)

    return render(
        request,
        "pages/forecast/forecast_plot.html",
        {"forecast_plot": line_plot, "current": consumable_name},
    )
