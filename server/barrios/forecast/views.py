from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from common.conditionalredirect import conditionalredirect
from data.models.ThresholdsLimitsDefinition import ThresholdsLimitsDefinition
from forecast.create_forecast_chart import create_forecast_chart
from forecast.create_forecast import create_forecast


def index(request):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    all_consumables = (
        ThresholdsLimitsDefinition.objects.filter(
            Q(threshold_owner="USOS") | Q(threshold_owner=None)
        )
        .values("threshold_category", "threshold_owner", "category_id")
        .distinct()
    )

    forecast_charts = []
    forecasts = []

    for consumable in all_consumables:
        if (
            consumable["threshold_category"] != "Water Alert"
            and consumable["threshold_category"] != "Water Critical"
        ):
            consumable_forecast = create_forecast(consumable["threshold_category"])
            consumable_forecast_chart = create_forecast_chart(
                consumable_forecast, with_title=False
            )
            forecasts.append(consumable_forecast)
            forecast_charts.append(consumable_forecast_chart)

    water_forecast = create_forecast("Water Alert")
    water_chart = create_forecast_chart(water_forecast, with_title=False)
    forecast_charts.append(water_chart)
    forecasts.append(water_forecast)

    forecasts = [
        {"title": f["consumable_name"], "chart": forecast_charts[idx]}
        for idx, f in enumerate(forecasts)
    ]

    return render(request, "pages/forecast/index.html", {"forecasts": forecasts})


def get_forecast(request, consumable_name):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    forecast_obj = create_forecast(consumable_name)
    line_plot = create_forecast_chart(forecast_obj)

    return render(
        request,
        "pages/forecast/forecast_plot.html",
        {
            "forecast_plot": line_plot,
            "current": consumable_name,
            "current_page": "forecast",
        },
    )


def get_all_forecasts(request):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")
