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

import numpy as np
import importlib

def insert_model(name, fields, values):
   params_dict = {}
   print(fields)
   print(values)
   for idx, f in np.ndenumerate(fields):
      # print(f'{idx}: f')
     key = f
     val = values[idx]
     print(f"{f}: {type(val)}: {val}")
     params_dict[key] = val
   
   ReturnClass = getattr(importlib.import_module(f'models.{name}'), name)
   # print(ReturnClass)
   try:
      insert_row = ReturnClass.create(params_dict)
   except Exception:
      pass

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