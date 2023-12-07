from django.shortcuts import render
from random import randint
from common.conditionalredirect import conditionalredirect
from forecast.create_forecast import create_forecast
from forecast.create_forecast_chart import create_forecast_chart
from optimization.Optimizer import Optimizer
from common.consumable_helpers import get_consumable_units
import datetime as dt

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
from common.consumable_helpers import get_consumable_names

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
        # We're intercepting the user's request here to make sure
        # they've loaded the necessary data to proceed. This should
        # probably be in a middleware.
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

        consumable_names = get_consumable_names()
        # forecast_obj = create_forecast("ACY Insert", dt.date(2022, 1, 14), dt.date(2023, 9, 5))
        # forecast_plot = create_forecast_chart(forecast_obj,)
        next_optimization = get_next_optimization(consumable_names)

        return render(
            request,
            "pages/dashboard/index.html",
            {
                "usage_difference": get_usage_average_difference(),
                "next_optimization": next_optimization,
                # "forecast_plot": forecast_plot,
                "consumable_names": consumable_names,
                "current": "ACY Insert",
            },
        )
    else:
        return conditionalredirect(request, "/accounts/login/")


def get_usage_average_difference():
    return randint(-10, 10)


def get_next_optimization(consumable_names: list[str]):
    next_optimization = {"date": None, "vehicle": None, "payload": []}

    for consumable in consumable_names:
        optimizer = Optimizer(consumable)
        next_optimization["date"] = optimizer.get_event_dates()[0].strftime("%m/%d/%Y")
        next_optimization["vehicle"] = optimizer.get_event_vehicles()[0]
        next_optimized_amount = optimizer.consumable_ascension()[0]
        item = {
            "name": consumable,
            "units": get_consumable_units(consumable),
            "amount": next_optimized_amount,
        }
        next_optimization["payload"].append((item))
    return next_optimization
