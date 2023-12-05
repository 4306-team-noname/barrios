import math
from datetime import date, datetime, timedelta
import pandas as pd
from django.db.models import Sum
from django.shortcuts import redirect, render
from data.models import IssFlightPlan, IssFlightPlanCrew, VehicleCapacityDef
from data.models.RatesDefinition import RatesDefinition
from optimization.forms import OptimizationForm
from optimization.Optimizer import Optimizer
from common.conditionalredirect import conditionalredirect
from common.consumable_helpers import get_consumable_names, get_consumable_units


# Okay, here's the plan:
# 1. Load a grid of missions to display on index.
#   - Each mission consists of:
#       - vehicle name
#       - launch date
#       - dock date
#       - Consumables/amounts table
# 2. Optimization form allows user to select a specific consumable
#    and sends a request to generate a single optimization for that item.
#    - Request's response is a chart showing how much of a given
#      consumable to ship on each launch date. The chart should include
#      thresholds ... I'm not sure what else. Considering that the optimization
#      will rely on calculated actual rates, it will essentially be a forecast
#      chart.


def index(request):
    # When the index is loaded, after checking whether the user is authenticated,
    # we create a new OptimizationForm object and pass it to the template to display
    # in the section's header. This form will make requests for a specific mission's optimized
    # shipment values.
    # We also run a complete optimization analysis and display the results in the
    # section's body.
    if request.user.is_authenticated:
        # Instantiate a new OptimizationForm object
        form = OptimizationForm()

        return render(request, "pages/optimization/index.html", {"form": form})
    else:
        return redirect("/accounts/login")


def missions(request):
    # Missions view on Optimizations page.
    # Displays a grid of missions with optimized
    # payloads.
    # Generate full analysis results.
    # 1. Get a list of all consumable names
    consumable_names = get_consumable_names()

    # This dict is what we'll package as a DataFrame
    # and use for plotting.
    current_optimization = {
        "event_date": [],
        "vehicle_name": [],
    }

    MIN_DATE = date.today()

    for consumable in consumable_names:
        optimizer = Optimizer(consumable, "Launch")
        quantities = optimizer.consumable_ascension()
        quantities_units = [
            f"{q} {get_consumable_units(consumable)}" for q in quantities
        ]
        fp_qs = IssFlightPlan.objects.filter(
            event="Launch", datedim__gte=MIN_DATE
        ).values("datedim", "vehicle_name")
        current_optimization["event_date"] = [d["datedim"] for d in fp_qs][:-1]
        current_optimization["vehicle_name"] = [v["vehicle_name"] for v in fp_qs][:-1]
        current_optimization[consumable] = quantities_units

    opt_df = pd.DataFrame(current_optimization)
    missions = opt_df.to_dict("records")

    return render(
        request,
        "pages/optimization/mission_grid.html",
        {"missions": missions},
    )


def consumables(request):
    # Consumables chart view on Optimizations page.
    # Generates a menu of buttons with a chart below.
    # The buttons are used to select which consumable
    # to generate an optimization chart for

    # Get consumable names to pass into
    # optimization chart interface
    # (populates consumable selection buttons)
    consumable_names = get_consumable_names()

    # Get the optimization for the first chart to be displayed
    optimizer = Optimizer("ACY Inserts")
    optimization_df = optimizer.get_optimization_dataframe()
    plot = optimizer.plot()

    return render(
        request,
        "pages/optimization/optimization_chart.html",
        {"consumable_names": consumable_names, "optimization_plot": plot},
    )


def get_optimization(request, consumable_name):
    # Returns an individual optimization chart
    # for a given consumable.
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    print(consumable_name)
    # Get single optimization for the given consumable
    optimizer = Optimizer(consumable_name)
    plot = optimizer.plot()

    return render(
        request,
        "components/optimization_plot.html",
        {"optimization_plot": plot, "current": consumable_name},
    )
