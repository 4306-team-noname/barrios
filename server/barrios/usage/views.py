from datetime import date, datetime
from django.shortcuts import redirect, render
from common.forms import AnalysisForm
from usage.charts import create_usage_chart
from common.conditionalredirect import conditionalredirect
from common.date_helpers import get_date_object
import pandas as pd
from data.models import (
    InventoryMgmtSystemConsumables,
    IssFlightPlanCrew,
    IssFlightPlanCrewNationalityLookup,
    RatesDefinition,
    UsRsWeeklyConsumableGasSummary,
    UsWeeklyConsumableWaterSummary,
)


def index(request):
    if request.user.is_authenticated:
        form = AnalysisForm()
        return render(
            request,
            "pages/usage/index.html",
            {"form": form},
        )
    else:
        return redirect("/accounts/login")


def analyze(request):
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
            consumable_name = str(consumable_name_obj)

            # get list of consumables
            rate_definition_value = RatesDefinition.objects.filter(
                affected_consumable=consumable_name,
                type="usage",
            ).values()

            actual_usage_values = []
            if consumable_name == "Water":
                actual_usage_values = UsWeeklyConsumableWaterSummary.objects.filter(
                    date__range=[start_date, end_date]
                ).values()
            elif (
                consumable_name == "Oxygen"
                or consumable_name == "Nitrogen"
                or consumable_name == "Air"
            ):
                actual_usage_values = UsRsWeeklyConsumableGasSummary.objects.filter(
                    date__range=[start_date, end_date]
                ).values()
            else:
                consumable_cat = RatesDefinition.objects.get(
                    affected_consumable=consumable_name
                )
                actual_usage_values = InventoryMgmtSystemConsumables.objects.filter(
                    category_id=consumable_cat.category
                ).values(
                    "datedim",
                    "ims_id",
                    "english_name",
                    "quantity",
                    "status",
                    "category",
                    "category_name",
                )
                # print(actual_usage_values)

                # return render(
                #     request,
                #     "pages/usage/result.html",
                #     {"error_message": "No analysis for that consumable yet."},
                # )

            usage_df: pd.DataFrame | None = None
            usage_chart = None

            if len(actual_usage_values) > 0:
                usage_df = pd.DataFrame(actual_usage_values)

            if usage_df is not None:
                if consumable_name == "Water":
                    usage_df = usage_df.drop(
                        columns=[
                            "corrected_potable_l",
                            "corrected_technical_l",
                            "resupply_potable_l",
                            "resupply_technical_l",
                        ]
                    )
                    usage_df = usage_df.rename(
                        columns={
                            "corrected_total_l": "actual_value",
                            "corrected_predicted_l": "predicted_value",
                        }
                    )

                    usage_chart = create_usage_chart(
                        {"consumable_name": consumable_name, "df": usage_df}
                    )

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
            # print(usage_chart)
            if usage_chart:
                return render(
                    request, "pages/usage/result.html", {"usage_chart": usage_chart}
                )
            else:
                return render(
                    request,
                    "pages/usage/result.html",
                    {"table_data": actual_usage_values},
                )
        else:
            return render(
                request, "pages/usage/result.html", {"error": "Invalid selection"}
            )
