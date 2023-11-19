from csv import DictReader
from cases import to_snake
from common.result import Result
from django.forms.models import model_to_dict


from .models import (
    Category,
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


class DataService:
    def keys_to_snake(self, model_dict):
        new_dict = {}
        for key in model_dict.keys():
            if "Unnamed" not in key:
                new_dict[to_snake(key)] = model_dict[key]
        return new_dict

    def read_and_insert_csv(self, model_name: str, csv_path: str) -> Result:
        insert_results = []
        with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = DictReader(file)
            for row in reader:
                converted = self.keys_to_snake(row)
                result = None

                if model_name == "ImsConsumablesCategoryLookup":
                    result = ImsConsumablesCategoryLookup.objects.create(**converted)
                    print(result)
                elif model_name == "InventoryMgmtSystemConsumables":
                    result = InventoryMgmtSystemConsumables.objects.create(**converted)
                elif model_name == "IssFlightPlan":
                    result = IssFlightPlan.objects.create(**converted)
                    print(result)
                elif model_name == "IssFlightPlanCrew":
                    result = IssFlightPlanCrew.objects.create(**converted)
                elif model_name == "IssFlightPlanCrewNationalityLookup":
                    result = IssFlightPlanCrewNationalityLookup.objects.create(
                        **converted
                    )
                elif model_name == "RatesDefinition":
                    result = RatesDefinition.objects.create(**converted)
                elif model_name == "RsaConsumableWaterSummary":
                    result = RsaConsumableWaterSummary.objects.create(**converted)
                elif model_name == "TankCapacityDefinition":
                    result = TankCapacityDefinition.objects.create(**converted)
                elif model_name == "ThresholdsLimitsDefinition":
                    result = ThresholdsLimitsDefinition.objects.create(**converted)
                elif model_name == "UsRsWeeklyConsumableGasSummary":
                    result = UsRsWeeklyConsumableGasSummary.objects.create(**converted)
                elif model_name == "UsWeeklyConsumableWaterSummary":
                    result = UsWeeklyConsumableWaterSummary.objects.create(**converted)
                if result is not None:
                    insert_results.append(result)
            if len(insert_results) > 0:
                serialized = [model_to_dict(result) for result in insert_results]
                return {"ok": True, "value": serialized}
            else:
                return {"ok": False, "error": "Unable to save records"}
