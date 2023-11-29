from django.shortcuts import render
from random import randint
from common.conditionalredirect import conditionalredirect
from forecast.create_forecast import create_forecast
from forecast.create_forecast_chart import create_forecast_chart

from data.models import (
    ImsConsumablesCategoryLookup,
    InventoryMgmtSystemConsumables,
    IssFlightPlan,
    IssFlightPlanCrew,
    IssFlightPlanCrewNationalityLookup,
    RatesDefinition,
    RsaConsumableWaterSummary,
    TankCapacityDefinition,
    ThresholdsLimitsDefinition,
    UsRsWeeklyConsumableGasSummary,
    UsWeeklyConsumableWaterSummary,
)

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
        required_models = [
            ImsConsumablesCategoryLookup,
            InventoryMgmtSystemConsumables,
            IssFlightPlan,
            IssFlightPlanCrew,
            IssFlightPlanCrewNationalityLookup,
            RatesDefinition,
            RsaConsumableWaterSummary,
            TankCapacityDefinition,
            ThresholdsLimitsDefinition,
            UsRsWeeklyConsumableGasSummary,
            UsWeeklyConsumableWaterSummary,
        ]

        missing_models_readable_names = []

        for model in required_models:
            if model.objects.count() == 0:
                print(f"missing model: {model.__name__}")
                missing_models_readable_names.append(model.readable_name)

        if len(missing_models_readable_names) > 0:
            request.session["missing_data"] = missing_models_readable_names
            return conditionalredirect(
                request,
                "/data/",
            )

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
