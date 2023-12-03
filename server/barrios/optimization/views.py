import math
from datetime import date, datetime, timedelta
from django.db.models import Sum
from django.shortcuts import redirect, render
from data.models import IssFlightPlan, IssFlightPlanCrew, VehicleCapacityDef
from data.models.RatesDefinition import RatesDefinition
from optimization.forms import OptimizationForm
from optimization.Optimizer import Optimizer


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
        # 1. Get a list of all consumable names
        consumable_names_values = (
            RatesDefinition.objects.order_by("affected_consumable")
            .distinct("affected_consumable")
            .values("affected_consumable")
        )
        consumable_names = [d["affected_consumable"] for d in consumable_names_values]
        for consumable in consumable_names:
            optimizer = Optimizer(consumable, "Dock")
            quantities = optimizer.consumable_ascension()
            print(quantities)
            # 1. Get a list of event dates
        # event_type = "Launch"
        # event_date_list = get_flightplan_event_dates(event_type)
        # # print(f"event_dates: {event_date_list}")
        #
        # optimization_results = {}
        # for consumable_name in consumable_names:
        #     optimized_values = consumable_ascension(consumable_name, event_date_list)
        #     optimization_results[consumable_name] = optimized_values
        #
        # optimization_results["event_dates"] = [
        #     event_date_list[i] for i in range(0, len(event_date_list) - 1)
        # ]
        # optimization_results["event_type"] = event_type
        #
        # optimization_results["vehicle_names"] = []
        # optimization_results["vehicle_types"] = []
        #
        # for event in optimization_results["event_dates"]:
        #     event_vehicle = IssFlightPlan.objects.filter(datedim=event).first()
        #     optimization_results["vehicle_names"].append(event_vehicle.vehicle_name)
        #     optimization_results["vehicle_types"].append(event_vehicle.vehicle_type)
        #
        # missions = []
        # for i in range(0, len(optimization_results["event_dates"])):
        #     mission = {
        #         "vehicle_name": optimization_results["vehicle_names"][i],
        #         "vehicle_type": optimization_results["vehicle_types"][i],
        #         "event_date": optimization_results["event_dates"][i],
        #         "event_type": optimization_results["event_type"],
        #         "payload": [],
        #     }
        #     for consumable_name in consumable_names:
        #         mission["payload"].append(
        #             {
        #                 "name": consumable_name,
        #                 "amount": optimization_results[consumable_name][i],
        #             }
        #         )
        #
        #     missions.append(mission)
        #
        # print(missions)

        return render(
            request,
            "pages/optimization/index.html",
            {"form": form},
            # {"form": form, "missions": missions},
        )
    else:
        return redirect("/accounts/login")


def consumable_ascension(consumable_name: str, event_date_list: list[date]):
    # 1. Get a list of days between launches
    event_deltas = get_flightplan_deltas(event_date_list)
    # print(f"deltas: {event_deltas}")
    # 2. Grab the number of event dates
    num_events = len(event_date_list) - 1
    crew_count_list = get_crew_per_event_date(event_date_list)
    # print(f"crew_count: {crew_count_list}")
    # print(
    #     f"num_events: {num_events}, num_deltas: {len(event_deltas)}, num_crew_counts: {len(crew_count_list)}"
    # )
    sum_generated, sum_usage, sum_usage_crew = get_assumed_rates(consumable_name)

    listofrates = [sum_usage] * (num_events)
    # print(f"list_of_rates: {listofrates}")
    listofrates_crew = []
    consumable_to_send = []
    current_sum = 0
    res_list = []

    for i in range(0, len(listofrates)):
        listofrates_crew.append(crew_count_list[i] * sum_usage_crew)
        res_list.append(
            ((listofrates[i] + listofrates_crew[i]) - sum_generated) * event_deltas[i]
        )

    for i, value in enumerate(res_list):
        current_sum += value
        consumable_to_send.append(math.trunc(current_sum))
        current_sum = current_sum - math.trunc(current_sum)

    return consumable_to_send


def get_assumed_rates(consumable_name: str):
    # Get the sum of rate values for a given consumable
    # Parameters:
    #  consumable_name: str
    #  The consumable to get the rate for

    # 1. Get the sum of rates with a rate type of 'generation'
    sum_generated_values = RatesDefinition.objects.filter(
        affected_consumable=consumable_name, type="generation"
    ).aggregate(Sum("rate"))

    if sum_generated_values["rate__sum"] is None:
        sum_generated = 0
    else:
        sum_generated = sum_generated_values["rate__sum"]

    # 2. Get the sum of rates with a rate type of 'usage' and
    #   units containing 'Crew/Day'
    sum_usage_with_crew_values = RatesDefinition.objects.filter(
        affected_consumable=consumable_name, type="usage", units__contains="Crew/Day"
    ).aggregate(Sum("rate"))

    if sum_usage_with_crew_values["rate__sum"] is None:
        sum_usage_crew = 0
    else:
        sum_usage_crew = sum_usage_with_crew_values["rate__sum"]

    # 3. Get the sum of rates with a rate type of 'usage' and
    #  units not containing 'Crew/Day'
    sum_usage_without_values = (
        RatesDefinition.objects.filter(
            affected_consumable=consumable_name, type="usage"
        )
        .exclude(units__contains="Crew/Day")
        .aggregate(Sum("rate"))
    )

    if sum_usage_without_values["rate__sum"] is None:
        sum_usage = 0
    else:
        sum_usage = sum_usage_without_values["rate__sum"]

    return sum_usage, sum_usage_crew, sum_generated


def get_crew_per_event_date(event_date_list: list[date]) -> list[int]:
    # Get a list of crew counts for a given list of event dates
    # Parameters:
    # event_date_list: list[date]
    #  A list of event dates to get crew counts for
    crew_count_list = []
    for event_date in event_date_list:
        crew_count = IssFlightPlanCrew.objects.filter(datedim=event_date).aggregate(
            Sum("crew_count")
        )
        crew_count_list.append(crew_count["crew_count__sum"])
    return crew_count_list


def get_flightplan_event_dates(event_type: str) -> list[date]:
    # Get a list of dates for a given event type
    # Parameters:
    #  event_type: str
    #    The event type to get dates for
    #    Valid values: 'Launch', 'Dock', 'Undock', 'Landing'
    event_date_values = IssFlightPlan.objects.filter(event=event_type).values("datedim")
    event_dates = [d["datedim"] for d in event_date_values]
    return event_dates


def get_flightplan_deltas(date_list: list[date]) -> list[int]:
    days_list = []
    for idx, d1 in enumerate(date_list):
        j = idx + 1
        if j < len(date_list):
            d2 = date_list[j]
            delta = d2 - d1
            days_list.append(delta.days)
    return days_list


# route: /optimization/analyze
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
