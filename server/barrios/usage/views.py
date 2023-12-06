from datetime import datetime
from django.shortcuts import redirect, render
from common.forms import AnalysisForm
from usage.Rater import Rater


def index(request):
    # When the index is loaded, after checking whether the user is authenticated,
    # we create a new AnalysisForm object and pass it to the template.
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
    # When the user submits the form, we check if the form is valid.
    # If it is, we can begin the analysis. If not, we redirect to the index.
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            # We receive a reference to the RatesDefinition object's
            # 'affected_consumable' field and a reference to the
            # UsWeeklyConsumableWaterSummary object's 'date' field.
            # Those will need to be converted into something that's usable
            # for additional queries. Each date field goes through two conversions. First,
            # it's converted to a datetime object. Then, it's converted to a string
            # that's formatted as YYYY-MM-DD.
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

            # Instantiate a Rater to handle our calculations
            # and generate our graphics
            rater = Rater(consumable_name, start_date_obj, end_date_obj)
            rate_object = rater.rate()
            actual_usage_values = rater.create_usage_dataframe()
            usage_chart = rater.plot()

            if usage_chart:
                return render(
                    request,
                    "pages/usage/result.html",
                    {"usage_chart": usage_chart, "rate_info": rate_object},
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
