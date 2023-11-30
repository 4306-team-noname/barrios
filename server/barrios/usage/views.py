from django.http import HttpResponse
from django.shortcuts import redirect, render
from random import randint
from .forms import UsageForm
from common.conditionalredirect import conditionalredirect
from data.models import InventoryMgmtSystemConsumables, RatesDefinition


def index(request):
    if request.user.is_authenticated:
        usage_difference = randint(-50, 50)
        return render(
            request,
            "pages/usage/index.html",
            {"usage_difference": usage_difference},
        )
    else:
        return redirect("/accounts/login")


def analyze(request):
    form = UsageForm(request.POST)
    print(form)
    if form.is_valid:
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        # get list of consumables
        rates_definitions_values = RatesDefinition.objects.all().values()
        assumed_rates = []
        ims_rate_items = []
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
