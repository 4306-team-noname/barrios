from models.ImsConsumablesCategoryLookupEntry import ImsConsumablesCategoryLookupEntry
from models.InventoryMgmtSystemConsumablesEntry import InventoryMgmtSystemConsumablesEntry
from models.IssFlightPlanEntry import IssFlightPlanEntry
from models.IssFlightPlanCrewEntry import IssFlightPlanCrewEntry
from models.IssFlightPlanCrewNationalityLookupEntry import IssFlightPlanCrewNationalityLookupEntry
from models.RatesDefinitionEntry import RatesDefinitionEntry
from models.RsaConsumableWaterSummaryEntry import RsaConsumableWaterSummaryEntry
from models.StoredItemsOnlyInventoryMgmtSystemConsumablesEntry import StoredItemsOnlyInventoryMgmtSystemConsumablesEntry
from models.TankCapacityDefinitionEntry import TankCapacityDefinitionEntry
from models.ThresholdsLimitsDefinitionEntry import ThresholdsLimitsDefinitionEntry
from models.UsRsWeeklyConsumableGasSummaryEntry import UsRsWeeklyConsumableGasSummaryEntry
from models.UsWeeklyConsumableWaterSummaryEntry import UsWeeklyConsumableWaterSummaryEntry
from models.Upload import Upload

import importlib

def insert_model(name, fields, values):
    params_dict = {}
    for i in fields:
      key = fields[i]
      val = values[i]
      params_dict[key] = val

    ReturnClass = getattr(importlib.import_module(f'models.{name}'), name)
    ReturnClass.create(params_dict)

def define_models(db):
   db.define_models(
      Upload,
      ImsConsumablesCategoryLookupEntry,
      InventoryMgmtSystemConsumablesEntry,
      IssFlightPlanEntry,
      IssFlightPlanCrewEntry,
      IssFlightPlanCrewNationalityLookupEntry,
      RatesDefinitionEntry,
      RsaConsumableWaterSummaryEntry,
      StoredItemsOnlyInventoryMgmtSystemConsumablesEntry,
      TankCapacityDefinitionEntry,
      ThresholdsLimitsDefinitionEntry,
      UsRsWeeklyConsumableGasSummaryEntry,
      UsWeeklyConsumableWaterSummaryEntry,
   )
   return db