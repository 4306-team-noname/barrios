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

from cases import to_snake
import numpy as np
import importlib
import datetime

def insert_model(name, fields, values):
    params_dict = {}

    for idx, f in np.ndenumerate(fields):
        key = to_snake(f)

        if key == 'date' or key == 'datedim' or key == 'report_date':
            val = datetime.datetime.strptime(values[idx], '%m/%d/%Y').date()
        else:
            val = values[idx]
        print(f"{key}: {type(val)}: {val}")
        params_dict[key] = val
   
    ReturnClass = getattr(importlib.import_module(f'models.{name}'), name)
    # print(ReturnClass)
    insert_row = ReturnClass.create(params_dict)

    if insert_row['id'] == None:
      error_key = list(insert_row['errors'])[0]
      return {'ok': False, 'error': insert_row['errors'][error_key], 'error_field': error_key}

    return {'ok': True, 'value': insert_row['id']}

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