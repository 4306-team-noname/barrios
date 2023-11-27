from common.result import Result
from data.core.csv_to_db import csv_to_db

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


def import_csv(model_name: str, filepath: str) -> Result:
    result = None
    if model_name == "ImsConsumablesCategoryLookup":
        result = csv_to_db(ImsConsumablesCategoryLookup, filepath)
    if model_name == "InventoryMgmtSystemConsumables":
        result = csv_to_db(InventoryMgmtSystemConsumables, filepath)
    elif model_name == "IssFlightPlan":
        result = csv_to_db(IssFlightPlan, filepath)
    elif model_name == "IssFlightPlanCrew":
        result = csv_to_db(IssFlightPlanCrew, filepath)
    elif model_name == "IssFlightPlanCrewNationalityLookup":
        result = csv_to_db(IssFlightPlanCrewNationalityLookup, filepath)
    elif model_name == "RatesDefinition":
        result = csv_to_db(RatesDefinition, filepath)
    elif model_name == "RsaConsumableWaterSummary":
        result = csv_to_db(RsaConsumableWaterSummary, filepath)
    elif model_name == "TankCapacityDefinition":
        result = csv_to_db(TankCapacityDefinition, filepath)
    elif model_name == "ThresholdsLimitsDefinition":
        result = csv_to_db(ThresholdsLimitsDefinition, filepath)
    elif model_name == "UsRsWeeklyConsumableGasSummary":
        result = csv_to_db(UsRsWeeklyConsumableGasSummary, filepath)
    elif model_name == "UsWeeklyConsumableWaterSummary":
        result = csv_to_db(UsWeeklyConsumableWaterSummary, filepath)
    if result:
        return {"ok": True, "value": result, "error": None}
    else:
        return {
            "ok": False,
            "value": None,
            "error": "There was an error saving your data.",
        }
