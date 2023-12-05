import pandas as pd
from pandas import DataFrame
import plotly.express as px
from django.db.models import Q
import datetime as dt
from data.models import UsWeeklyConsumableWaterSummary


class Rater:
    consumable: str
    min_date: dt.date
    max_date: dt.date
    rates_definition: DataFrame
    ims_consumables: DataFrame
    weekly_gas_summary: DataFrame
    weekly_water_summary: DataFrame
    crew_flight_plan: DataFrame

    def __init__(
        self, consumable: str, min_date=dt.date(2022, 1, 1), max_date=dt.date.today()
    ) -> None:
        """
        Initialize an instance with the name of the consumable
        to rate, a min_date with a default of 1/1/2022, and
        a max_date with a default of today.
        """
        self.consumable = consumable
        self.min_date = min_date
        self.max_date = max_date
        if self.consumable.lower() == "water":
            self.init_water_data()
        pass

    def rate(self):
        assumed_rate = None
        actual_rate = None
        delta_days = (self.max_date - self.min_date).days
        if self.consumable.lower() == "water":
            actual_rate = self.get_water_rate("actual")
            assumed_rate = self.get_water_rate("assumed")

        return {
            "assumed_rate_per_day": round(assumed_rate, 2),
            "actual_rate_per_day": round(actual_rate, 2),
            "days_sampled": delta_days,
        }

    def get_ims_rate(self):
        pass

    def get_gas_rate(self):
        pass

    def get_water_rate(self, type: str):
        field = None
        if type == "actual":
            field = "corrected_total_l"
        else:
            field = "corrected_predicted_l"

        resupply_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            Q(date__gte=self.min_date),
            Q(date__lte=self.max_date),
            Q(resupply_potable_l__gte=1),
        ).values("date")

        resupply_dates = [q["date"] for q in resupply_qs]
        print(f"resupply_dates: {resupply_dates}")

        usage_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            Q(date__gte=self.min_date),
            Q(date__lte=self.max_date),
        ).values("date", field)

        resupply_partitions = []
        current_partition = []

        if len(resupply_dates) == 0:
            for q in usage_qs:
                current_partition.append(q[field])
            print(f"current partition: {current_partition}")
            resupply_partitions.append(current_partition)
        else:
            for q in usage_qs:
                if q["date"] not in resupply_dates:
                    current_partition.append(q[field])
                else:
                    current_partition.append(q[field])
                    resupply_partitions.append(current_partition)
                    current_partition = []

        usage_rates = [
            (-1) * (partition[-1] - partition[0]) / (len(partition) - 1)
            for partition in resupply_partitions
        ]

        rate_deltas = [len(partition) for partition in resupply_partitions]

        print(f"usage rates: {usage_rates}")
        print(f"deltas: {rate_deltas}")

        average_weekly_usage_rate = sum(usage_rates) / len(usage_rates)
        average_daily_usage_rate = average_weekly_usage_rate / 7
        # print(f"{field} rates: {usage_rates}")
        #
        # usage_vals = [u[field] for u in usage_qs]
        # usage_over_time = usage_vals[0] - usage_vals[-1]
        # delta = self.max_date - self.min_date
        # return usage_over_time / delta.days
        return average_daily_usage_rate

    def plot(self):
        pass

    def init_water_data(self):
        water_summary_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            Q(date__gte=self.min_date), Q(date__lte=self.max_date)
        ).values()
        self.weekly_water_summary = pd.DataFrame.from_records(
            water_summary_qs, index="date"
        )
        pass
