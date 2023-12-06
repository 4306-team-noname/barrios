from django.http import HttpResponse
from django.shortcuts import render
from common.conditionalredirect import conditionalredirect
from data.models.ThresholdsLimitsDefinition import ThresholdsLimitsDefinition
from forecast.create_forecast_chart import create_forecast_chart
from forecast.create_forecast import create_forecast
from common.forms import AnalysisForm
from datetime import datetime


def index(request):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    form = AnalysisForm()
    return render(request, "pages/forecast/index.html", {"form": form})


def get_forecast(request, consumable_name):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            start_date_obj = datetime.strptime(
                str(form.cleaned_data["start_date"]), "%m/%d/%Y"
            )
            start_date = start_date_obj.strftime("%Y-%m-%d")
            end_date_obj = datetime.strptime(
                str(form.cleaned_data["end_date"]), "%m/%d/%Y"
            )
            end_date = end_date_obj.strftime("%Y-%m-%d")
            consumable_name_obj = form.cleaned_data["consumable_name"]
            # consumable_name can just be cast directly
            consumable_name = str(consumable_name_obj)

            model, forecast = create_forecast(consumable_name, start_date, end_date)  # type: ignore
            forecast_plot = create_forecast_chart(model, forecast)

            return render(
                request,
                "components/forecast_plot.html",
                {
                    "forecast_plot": forecast_plot,
                    "current": consumable_name,
                },
            )


def get_all_forecasts(request):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")


def analyze(request):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            start_date_obj = datetime.strptime(
                str(form.cleaned_data["start_date"]), "%m/%d/%Y"
            )
            start_date = start_date_obj.strftime("%Y-%m-%d")
            end_date_obj = datetime.strptime(
                str(form.cleaned_data["end_date"]), "%m/%d/%Y"
            )
            end_date = end_date_obj.strftime("%Y-%m-%d")
            consumable_name_obj = form.cleaned_data["consumable_name"]
            # consumable_name can just be cast directly
            consumable_name = str(consumable_name_obj)

            forecast_result = create_forecast(consumable_name, start_date, end_date)  # type: ignore
            # print(forecast_result)
            forecast_chart = create_forecast_chart(
                forecast_result["model"], forecast_result["forecast"]
            )

            return render(
                request,
                "pages/forecast/result.html",
                {
                    "forecast_chart": forecast_chart,
                    "current": consumable_name,
                },
            )
        else:
            return conditionalredirect(request, "/forecast/")
