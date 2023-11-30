from django.http import HttpResponse
from django.shortcuts import redirect, render
from random import randint
from .forms import UsageForm
from common.conditionalredirect import conditionalredirect
from datetime import date
from data.models import (
    InventoryMgmtSystemConsumables,
    RatesDefinition,
    UsWeeklyConsumableWaterSummary,
)


def index(request):
    if request.user.is_authenticated:
        form = UsageForm()
        return render(
            request,
            "pages/usage/index.html",
            {"form": form},
        )
    else:
        return redirect("/accounts/login")


def analyze(request):
    if request.htmx.boosted:
        print("This is a boosted request")
    if request.method == "POST":
        form = UsageForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            consumable_name = form.cleaned_data["consumable_name"]
            print(
                f"start_date: {start_date}, end_date: {end_date}, consumable_name: {consumable_name}"
            )

            # get list of consumables
            rates_definitions_values = RatesDefinition.objects.all().values()
            # for each:
            # - if consumable has category_id
            #   query InventoryMgmtSystemConsumables
            #   and begin calculation
            # - else, determine if it is water, gas, etc.
            #   and calculate usage from appropriate model
            # - also, get assumed usage rate from RatesDefinitions
            #   and calculate difference as a time series
            #     - This can be displayed on a line chart with the actual
            #       number of items(?)
            return render(
                request, "pages/usage/result.html", {"start_date": start_date}
            )
        else:
            return render(
                request, "pages/usage/result.html", {"error": "Invalid selection"}
            )
