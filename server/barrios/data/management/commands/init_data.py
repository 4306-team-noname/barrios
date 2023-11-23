from django.core.management.base import BaseCommand, CommandError
from data.models import (
    Category,
    Consumable,
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


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 1. Read the contents of a predefined folder
        # 2. For each file:
        #   -Check if the file matches something
        #    in the data dictionary
        #   -If yes, add the data
        #   -If no, print that the file is unknown
        # 3. Keep a list of models inserted into the db
        #   -If any models are missing, warn the user
        pass
