from models.ImsConsumablesCategoryLookup import ImsConsumablesCategoryLookup
from models.InventoryMgmtSystemConsumables import InventoryMgmtSystemConsumables
from models.IssFlightPlan import IssFlightPlan
from models.IssFlightPlanCrew import IssFlightPlanCrew
from models.IssFlightPlanCrewNationalityLookup import IssFlightPlanCrewNationalityLookup
from models.RatesDefinition import RatesDefinition
from models.RsaConsumableWaterSummary import RsaConsumableWaterSummary
from models.StoredItemsOnlyInventoryMgmtSystemConsumables import (
    StoredItemsOnlyInventoryMgmtSystemConsumables,
)
from models.TankCapacityDefinition import TankCapacityDefinition
from models.ThresholdsLimitsDefinition import ThresholdsLimitsDefinition
from models.UsRsWeeklyConsumableGasSummary import UsRsWeeklyConsumableGasSummary
from models.UsWeeklyConsumableWaterSummary import UsWeeklyConsumableWaterSummary

# from models.CategoryRatesLookup import CategoryRatesLookup
from models.Upload import Upload

from cases import to_snake
import numpy as np
import importlib
import datetime


def insert_model(name, fields, values):
    params_dict = {}

    for idx, f in np.ndenumerate(fields):
        key = to_snake(f)

        if key == "date" or key == "datedim" or key == "report_date":
            val = datetime.datetime.strptime(values[idx], "%m/%d/%Y").date()
        else:
            val = values[idx]
        print(f"{key}: {type(val)}: {val}")
        params_dict[key] = val

    ReturnClass = getattr(importlib.import_module(f"models.{name}"), name)
    # print(ReturnClass)
    insert_row = ReturnClass.create(params_dict)

    if insert_row["id"] is None:
        error_key = list(insert_row["errors"])[0]
        return {
            "ok": False,
            "error": insert_row["errors"][error_key],
            "error_field": error_key,
        }

    return {"ok": True, "value": insert_row["id"]}


def define_models(db):
    db.define_models(
        # CategoryRatesLookup,
        Upload,
        ImsConsumablesCategoryLookup,
        InventoryMgmtSystemConsumables,
        IssFlightPlan,
        IssFlightPlanCrew,
        IssFlightPlanCrewNationalityLookup,
        RatesDefinition,
        RsaConsumableWaterSummary,
        StoredItemsOnlyInventoryMgmtSystemConsumables,
        TankCapacityDefinition,
        ThresholdsLimitsDefinition,
        UsRsWeeklyConsumableGasSummary,
        UsWeeklyConsumableWaterSummary,
    )
    return db
