from django.http import HttpResponse
from django.shortcuts import redirect, render
from random import randint
from .forms import UsageForm
from common.conditionalredirect import conditionalredirect
<<<<<<< HEAD
from data.models import InventoryMgmtSystemConsumables, RatesDefinition
=======
from datetime import date
from data.models import (
    InventoryMgmtSystemConsumables,
    RatesDefinition,
    UsWeeklyConsumableWaterSummary,
)
>>>>>>> 3742991243eb8b4ccb42c3834f0d62f623d9a0db


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
<<<<<<< HEAD
    form = UsageForm(request.POST)
    print(form)
    if form.is_valid:
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        # get list of consumables
        rates_definitions_values = RatesDefinition.objects.all().values()
        assumed_rates = []
        for rate_definition in rates_definitions_values:
            if rate_definition["type"] != "generation":
                assumed_rates.append(rate_definition)
                print(rate_definition)
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
        return conditionalredirect(request, "/usage/")
=======
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
>>>>>>> 3742991243eb8b4ccb42c3834f0d62f623d9a0db
