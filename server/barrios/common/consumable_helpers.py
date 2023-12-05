from data.models import RatesDefinition, ThresholdsLimitsDefinition
from django.db.models import Q
from math import ceil, floor


def get_consumable_names() -> list[str]:
    # Queries for all consumables, excluding consumables
    # owned by RSA.
    #
    # Returns:
    #   list[str] :: List of consumable names
    consumable_names_values = (
        RatesDefinition.objects.order_by("affected_consumable")
        .distinct("affected_consumable")
        .exclude(affected_consumable="RS Food Rations")
        .values("affected_consumable")
    )
    consumable_names = [d["affected_consumable"] for d in consumable_names_values]
    return consumable_names


def get_consumable_units(consumable_name):
    consumable_qs = RatesDefinition.objects.filter(
        affected_consumable=consumable_name
    ).values("units")[0]
    return consumable_qs["units"]


def get_consumable_thresholds(consumable_name):
    critical_value = None
    print(f"forecast consumable name: {consumable_name}")

    if consumable_name.lower() == "water":
        water_values = ThresholdsLimitsDefinition.objects.filter(
            Q(threshold_category="Water Alert") | Q(threshold_category="Water Critical")
        ).values()
        threshold = water_values[0]
        critical_value = water_values[1]["threshold_value"]
    elif consumable_name.lower() == "air":
        threshold = {"threshold_value": 0}
    else:
        threshold = list(
            ThresholdsLimitsDefinition.objects.filter(
                threshold_category=consumable_name
            ).values()
        )[0]

    threshold_value = threshold["threshold_value"]
    threshold_plus_value = threshold_value + threshold_value * 0.1

    max_value = int(ceil(threshold_value * 1.25))
    min_value = int(floor(threshold_plus_value * 0.9))

    return {
        "threshold_value": threshold_value,
        "threshold_plus_value": threshold_plus_value,
        "max_value": max_value,
        "min_value": min_value,
        "critical_value": critical_value,
    }
