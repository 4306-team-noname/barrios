from datetime import date, datetime, timedelta
from django.shortcuts import redirect, render
from data.models import IssFlightPlan
from data.models.VehicleCapacityDef import VehicleCapacityDef
from optimization.forms import OptimizationForm


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
        # Generate full analysis results.
        return render(request, "pages/optimization/index.html", {"form": form})
    else:
        return redirect("/accounts/login")


def analyze(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = OptimizationForm(request.POST)
            if not form.is_valid():
                return render(request, "pages/optimization/index.html", {"form": form})
            if form.is_valid():
                print(f"cleaned_data: {form.cleaned_data}")
                mission = form.cleaned_data["mission"].vehicle_name
                mission_values = IssFlightPlan.objects.filter(
                    vehicle_name=mission
                ).values("datedim", "vehicle_name", "vehicle_type", "event")

                if len(mission_values) > 0:
                    mission_info = {
                        "vehicle_name": mission,
                        "vehicle_type": None,
                        "launch_date": None,
                        "dock_date": None,
                        "undock_date": None,
                        "landing_date": None,
                    }

                    for value in mission_values:
                        mission_info["vehicle_type"] = value["vehicle_type"]

                        if value["event"] == "Launch":
                            mission_info["launch_date"] = value["datedim"]
                        elif value["event"] == "Dock":
                            mission_info["dock_date"] = value["datedim"]
                        elif value["event"] == "Undock":
                            mission_info["undock_date"] = value["datedim"]
                        elif value["event"] == "Landing":
                            mission_info["landing_date"] = value["datedim"]

                    capacity_values = (
                        VehicleCapacityDef.objects.filter(
                            vehicle__in=mission_info["vehicle_type"],
                        ).values()
                        | VehicleCapacityDef.objects.filter(
                            vehicle__in=mission_info["vehicle_name"]
                        ).values()
                    )
                    print(capacity_values)
                    return render(
                        request,
                        "pages/optimization/optimization_result.html",
                        {"mission_info": mission_info},
                    )
        else:
            return redirect("/optimization")


def get_optimization(request, consumable):
    # The following call to IssFlightPlan.objects.filter()
    # is equivalent to:
    # SELECT datedim FROM iss_flight_plan WHERE event = 'Dock';
    docking_date_values = IssFlightPlan.objects.filter(event="Dock").values("datedim")

    # The above query returns a list of dicts that looks like
    # {'datedim': datetime.date(2022, 2, 17)}, so we can use
    # list comprehension to reduce that to a list of
    # datetime objects.
    docking_dates = [d["datedim"] for d in docking_date_values]
    print(f"{len(docking_dates)} docking_dates found: {docking_dates}")

    # Sweet, we have a list of date objects. Let's use that
    # to get a list of the number of days between
    # docking dates. (I extracted that logic into its
    # own function -- below this function.)
    deltas_list = get_flightplan_deltas(docking_dates)
    print(f"deltas_list: {deltas_list}")
    # ideally, we'd check whether we have any errors
    # here and either raise an exception or render a template
    # For now, let's just pass.
    pass


def get_flightplan_deltas(date_list: list[date]) -> list[int]:
    days_list = []
    for idx, d1 in enumerate(date_list):
        j = idx + 1
        if j < len(date_list):
            d2 = date_list[j]
            delta = d2 - d1
            days_list.append(delta.days)
    return days_list
