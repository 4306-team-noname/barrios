from common.flight_plan_crew_helpers import (
    get_usos_crew_by_date,
    get_commercial_crew_by_date,
)
from django.db.models.query import Cast
import pandas as pd
import numpy as np
from pandas import DataFrame
import plotly.graph_objs as go
from django.db.models import Q, Sum
import datetime as dt
import pytz
from data.models import (
    InventoryMgmtSystemConsumables,
    UsWeeklyConsumableWaterSummary,
    UsRsWeeklyConsumableGasSummary,
)
from data.models.IssFlightPlan import IssFlightPlan
from data.models.RatesDefinition import RatesDefinition
from common.flight_plan_crew_helpers import (
    get_total_crew_by_date,
)
from common.consumable_helpers import get_consumable_names
from django.utils.timezone import make_aware


class Rater:
    WATER_UNIT = "liters"
    GAS_UNIT = "lbs"
    consumable: str
    min_date: dt.date
    aware_min_date: dt.datetime
    max_date: dt.date
    aware_max_date: dt.datetime
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
        self.consumable = consumable.lower()
        self.min_date = min_date
        min_dt = dt.datetime.combine(min_date, dt.datetime.min.time())
        timezone = pytz.timezone("US/Central")
        self.aware_min_date = make_aware(min_dt, timezone)
        self.max_date = max_date
        max_dt = dt.datetime.combine(max_date, dt.datetime.min.time())
        self.aware_max_date = make_aware(max_dt, timezone)
        if self.consumable.lower() == "water":
            self.init_water_data()
        pass

    def rate(self):
        consumable = self.consumable.lower()
        assumed_rate = self.rate_assumed()
        actual_rate = self.rate_actual()
        predicted_rate = self.rate_predicted()
        delta_days = (self.max_date - self.min_date).days
        unit = self.get_consumable_unit()

        return {
            "unit": unit,
            "assumed_rate_per_day": round(assumed_rate, 2) if assumed_rate else None,
            "predicted_rate_per_day": round(predicted_rate, 2)
            if predicted_rate
            else None,
            "actual_rate_per_day": round(actual_rate, 2) if actual_rate else None,
            "days_sampled": delta_days,
        }

    def get_consumable_unit(self):
        # Shamefully hardcoding unit values
        if self.consumable == "water":
            unit = "liters"
        elif self.consumable == "air" or self.consumable == "nitrogen" or self.consumable == "oxygen":
            unit = "lbs"
        elif self.consumable == "acy inserts":
            unit = "inserts"
        elif self.consumable == "kto":
            unit = "kto"
        elif self.consumable == "us food bobs":
            unit = "bob"
        elif self.consumable == "filter inserts":
            unit = "insert filter"
        elif self.consumable == "pretreat tank":
            unit = "pretreat"
        elif self.consumable == "urine receptacle":
            unit = "urine receptacle"
        else:
            unit = ""

        return unit

    def rate_actual(self):
        if self.consumable == "water":
            return self.get_actual_water_rate()
        elif self.consumable in ["oxygen", "nitrogen", "air"]:
            return self.get_actual_gas_rate()
        else:
            return self.get_actual_ims_rate()

    def rate_assumed(self):
        if self.consumable == "water":
            return self.get_assumed_water_rate()
        elif self.consumable in ["oxygen", "nitrogen", "air"]:
            return self.get_assumed_gas_rate()
        else:
            return self.get_assumed_ims_rate()

    def rate_predicted(self):
        return self.get_predicted_water_rate() if self.consumable == "water" else None

    def get_actual_ims_rate(self):
        consumable_cat = RatesDefinition.objects.get(
            affected_consumable__istartswith=self.consumable
        )
        ims_qs = InventoryMgmtSystemConsumables.objects.filter(
            (Q(status="Installed") | Q(status="Stowed")),
            category_id=consumable_cat.category,
            datedim__range=[self.aware_min_date, self.aware_max_date],
        ).values("datedim", "ims_id", "quantity", "status", "category", "category_name")

        df = pd.DataFrame.from_records(ims_qs)

        df_dd_group = df.groupby(["datedim"]).agg({"quantity": "sum"})
        qtys = list(df_dd_group["quantity"])
        usages = []
        for idx, qty in enumerate(qtys[:-1]):
            if qtys[idx + 1] < qty:
                usages.append(qty - qtys[idx + 1])
        usage_rate = sum(usages) / len(usages)

        return usage_rate

    def get_actual_gas_rate(self):
        if self.consumable == "oxygen":
            resupply_qs = UsRsWeeklyConsumableGasSummary.objects.filter(
                Q(resupply_o2_kg__gte=1),
                date__range=[self.min_date, self.max_date],
            ).values("date")
            usage_qs = UsRsWeeklyConsumableGasSummary.objects.filter(
                date__range=[self.min_date, self.max_date]
            ).values("date", "adjusted_o2_kg")
            field = "adjusted_o2_kg"
        elif self.consumable == "nitrogen":
            resupply_qs = UsRsWeeklyConsumableGasSummary.objects.filter(
                Q(resupply_n2_kg__gte=1),
                date__range=[self.min_date, self.max_date],
            ).values("date")
            usage_qs = UsRsWeeklyConsumableGasSummary.objects.filter(
                date__range=[self.min_date, self.max_date]
            ).values("date", "adjusted_n2_kg")
            field = "adjusted_n2_kg"
        else:  # consumable == 'air'
            resupply_qs = UsRsWeeklyConsumableGasSummary.objects.filter(
                Q(resupply_air_kg__gte=1),
                date__range=[self.min_date, self.max_date],
            ).values("date")
            usage_qs = UsRsWeeklyConsumableGasSummary.objects.filter(
                date__range=[self.min_date, self.max_date]
            ).values("date", "adjusted_o2_kg", "adjusted_n2_kg")
            field = "air"

        # Flatten the resupply_dates CopyQueryset into a list of dates
        resupply_dates = [q["date"] for q in resupply_qs]

        # We need to calculate the average rate between
        # resupplies. We'll iterate through all usage records
        # and add them to 'current_partition.' When we hit a resupply
        # date, append the current partition to 'resupply_partitions'
        # and reset current_partition to an empty list.
        resupply_partitions = []
        current_partition = []

        if len(resupply_dates) == 0:
            for q in usage_qs:
                if field == "air":
                    current_partition.append(
                        (q["adjusted_o2_kg"] * 0.2)
                        + (q["adjusted_n2_kg"] * 0.8) * 2.20462
                    )
                else:
                    current_partition.append(q[field] * 2.20462)
            resupply_partitions.append(current_partition)
        else:
            for q in usage_qs:
                if q["date"] not in resupply_dates:
                    if field == "air":
                        current_partition.append(
                            (q["adjusted_o2_kg"] * 0.2)
                            + (q["adjusted_n2_kg"] * 0.8) * 2.20462
                        )
                    else:
                        current_partition.append(q[field] * 2.20462)
                else:
                    if field == "air":
                        current_partition.append(
                            (q["adjusted_o2_kg"] * 0.2)
                            + (q["adjusted_n2_kg"] * 0.8) * 2.20462
                        )
                    else:
                        current_partition.append(q[field] * 2.20462)
                    resupply_partitions.append(current_partition)
                    current_partition = []

        # Calculate the average weekly rate between resupplies.
        # This will be a list of len(1), but we'll take care of
        # that momentarily, when we sum/divide for the next variable.
        usage_rates = [
            (partition[0] - partition[1]) / (len(partition) - 1)
            if len(partition) > 1
            else 1  # avoid division by zero
            for partition in resupply_partitions
        ]

        average_weekly_usage_rate = sum(usage_rates) / len(usage_rates)
        average_daily_usage_rate = average_weekly_usage_rate / 7
        return average_daily_usage_rate

    def get_actual_water_rate(self):
        """
        Calculates the actual daily water usage according to weekly
        reported values on the space station.
        """
        # We're querying against the actual reported
        # water levels on the ISS — 'corrected_total_l'
        field = "corrected_total_l"

        # Get a set of the days in which 'resupply_potable_l'
        # is at least 1.
        resupply_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            Q(resupply_potable_l__gte=1),
            date__range=[self.min_date, self.max_date],
        ).values("date")

        usage_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            date__range=[self.min_date, self.max_date]
        ).values("date", field)

        resupply_dates = [q["date"] for q in resupply_qs]

        # Iterate through all usage records
        # and add them to 'current_partition.' When we hit a resupply
        # date, append the current partition to 'resupply_partitions'
        # and reset current_partition to an empty list.
        resupply_partitions = []
        current_partition = []

        if len(resupply_dates) == 0:
            for q in usage_qs:
                current_partition.append(q[field])
            resupply_partitions.append(current_partition)
        else:
            for q in usage_qs:
                if q["date"] not in resupply_dates:
                    current_partition.append(q[field])
                else:
                    current_partition.append(q[field])
                    resupply_partitions.append(current_partition)
                    current_partition = []

        # Calculate the average weekly rate between resupplies.
        # This will be a list of len(1), but we'll take care of
        # that momentarily, when we sum/divide for the next variable.
        usage_rates = [
            (-1) * (partition[-1] - partition[0]) / (len(partition) - 1)
            if len(partition) > 1
            else 1  # avoid division by zero
            for partition in resupply_partitions
        ]

        average_weekly_usage_rate = sum(usage_rates) / len(usage_rates)
        average_daily_usage_rate = average_weekly_usage_rate / 7
        return average_daily_usage_rate

    def get_assumed_gas_rate(self):
        if self.consumable == "oxygen":
            oxygen_generation_rate = RatesDefinition.objects.filter(
                Q(affected_consumable="Oxygen"), Q(type="generation")
            ).aggregate(total=Sum("rate"))["total"]

            oxygen_flat_consumption_rate = RatesDefinition.objects.filter(
                Q(affected_consumable="Oxygen"), Q(type="usage")
            ).aggregate(total=Sum("rate"))["total"]

            oxygen_crew_consumption_rate = RatesDefinition.objects.filter(
                Q(affected_consumable="Oxygen"), Q(type="usage"), units__contains="Crew"
            ).aggregate(total=Sum("rate"))["total"]

            daily_crew_rates = []
            delta = dt.timedelta(days=1)
            current_date = self.min_date

            while current_date <= self.max_date:
                total_crew_count = get_total_crew_by_date(current_date)
                # usos_crew_count = get_usos_crew_by_date(current_date)
                daily_crew_rates.append(
                    (total_crew_count + oxygen_crew_consumption_rate)
                )
                # daily_crew_rates.append((usos_crew_count + water_crew_consumption_rate))
                current_date += delta

            real_crew_rate = sum(daily_crew_rates) / len(daily_crew_rates)
            # water_generation_rate = 0
            total_consumption_rate = (
                real_crew_rate + oxygen_flat_consumption_rate
            ) - oxygen_generation_rate
            return total_consumption_rate

        elif self.consumable == "nitrogen":
            return RatesDefinition.objects.filter(
                Q(affected_consumable="Nitrogen"), Q(type="usage")
            ).aggregate(total=Sum("rate"))["total"]
        elif self.consumable == "air":
            air_flat_consumption_rate = RatesDefinition.objects.filter(
                Q(affected_consumable="Air"), Q(type="usage"), units__contains="Day"
            ).aggregate(total=Sum("rate"))["total"]

            air_eva_consumption_rate = RatesDefinition.objects.filter(
                Q(affected_consumable="Air"), Q(type="usage"), units__contains="EVA"
            ).aggregate(total=Sum("rate"))["total"]

            num_evas = IssFlightPlan.objects.filter(
                event="EVA", datedim__range=[self.min_date, self.max_date]
            ).count()

            total_eva_consumption = num_evas * air_eva_consumption_rate
            eva_rate_per_day = (
                total_eva_consumption / (self.max_date - self.min_date).days
            )
            rate = air_flat_consumption_rate + eva_rate_per_day
            return rate

    def get_assumed_ims_rate(self):
        rates_qs = RatesDefinition.objects.filter(
            Q(affected_consumable__iexact=self.consumable), Q(type="usage")
        ).values("rate", "units")

        flat_rates = []
        crew_rates = []

        for q in rates_qs:
            if "Crew" in q["units"]:
                crew_rates.append(q["rate"])
            else:
                flat_rates.append(q["rate"])

        if len(flat_rates) > 0:
            flat_rate = sum(flat_rates) / len(flat_rates)
        else:
            flat_rate = 0

        if len(crew_rates) > 0:
            usos_counts = []
            for date in pd.date_range(self.min_date, self.max_date):
                usos_counts.append(get_usos_crew_by_date(date))
            mean_crew = sum(usos_counts) / len(usos_counts)
            adjusted_crew_rates = [rate + mean_crew for rate in crew_rates]
            crew_rate = sum(adjusted_crew_rates) / len(adjusted_crew_rates)
        else:
            crew_rate = 0

        # print(f"assumed_rate: {flat_rate + crew_rate}")
        return flat_rate + crew_rate

    def get_assumed_water_rate(self):
        water_generation_rate = RatesDefinition.objects.filter(
            Q(affected_consumable="Water"), Q(type="generation")
        ).aggregate(total=Sum("rate"))["total"]

        water_flat_consumption_rate = RatesDefinition.objects.filter(
            Q(affected_consumable="Water"), Q(type="usage"), units="Liters/Day"
        ).aggregate(total=Sum("rate"))["total"]

        water_crew_consumption_rate = RatesDefinition.objects.filter(
            Q(affected_consumable="Water"), Q(type="usage"), units__contains="Crew"
        ).aggregate(total=Sum("rate"))["total"]

        daily_crew_rates = []
        delta = dt.timedelta(days=1)
        current_date = self.min_date

        while current_date <= self.max_date:
            total_crew_count = get_total_crew_by_date(current_date)
            # usos_crew_count = get_usos_crew_by_date(current_date)
            daily_crew_rates.append((total_crew_count + water_crew_consumption_rate))
            # daily_crew_rates.append((usos_crew_count + water_crew_consumption_rate))
            current_date += delta

        real_crew_rate = sum(daily_crew_rates) / len(daily_crew_rates)
        # water_generation_rate = 0
        total_consumption_rate = (
            real_crew_rate + water_flat_consumption_rate
        ) - water_generation_rate
        return total_consumption_rate

    def get_predicted_water_rate(self):
        """
        Calculates the predicted usage rate from weekly reporting in UsWeeklyConsumableWaterSummary.
        """
        # Get all 'corrected_predicted_l' from weekly water report within
        # min_date and max_date
        predicted_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            date__range=[self.min_date, self.max_date]
        ).values("corrected_predicted_l")

        predicted_usages = [q["corrected_predicted_l"] for q in predicted_qs]
        average_weekly_rate = (predicted_usages[0] - predicted_usages[-1]) / len(
            predicted_usages
        )
        return average_weekly_rate / 7

    def plot(self):
        df = self.create_usage_dataframe()
        consumable_name = self.consumable
        fig = go.Figure()

        fig.update_layout(
            paper_bgcolor="#091D41",
            plot_bgcolor="#091D41",
            title_font_color="#ffffff",
            legend_font_color="#ffffff",
            margin=dict(t=32, r=8, b=8, l=8),
            font=dict(color="#ffffff"),
            hovermode="x",
            newshape_layer="below",
        )

        fig.update_xaxes(
            showline=True,
            linewidth=1,
            linecolor="#5d7bb0",
            gridcolor="#5d7bb0",
        )

        fig.update_yaxes(
            showline=True,
            linewidth=1,
            linecolor="#5d7bb0",
            gridcolor="#5d7bb0",
        )

        fig.update_layout(title={"text": consumable_name.upper()})

        fig.add_trace(
            go.Scatter(
                x=list(df["date"]),
                y=list(df["actual_value"]),
                name="Actual",
                line=dict(color="#dade35", width=2),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=list(df["date"]),
                y=list(df["predicted_value"]),
                name="Predicted",
                line=dict(color="#ffffff", width=2),
            )
        )
        line_plot = fig.to_html(
            config={"displayModeBar": False, "responsive": True},
            full_html=False,
            # default_height=600,
            # include_plotlyjs=False,
            include_mathjax=False,
        )
        return line_plot

    def create_usage_dataframe(self):
        start_date = self.min_date
        end_date = self.max_date

        if self.consumable == "water":
            actual_usage_values = UsWeeklyConsumableWaterSummary.objects.filter(
                date__range=[start_date, end_date]
            ).values()
        elif self.consumable in ["oxygen", "nitrogen"]:
            actual_usage_values = UsRsWeeklyConsumableGasSummary.objects.filter(
                date__range=[start_date, end_date]
            ).values()
        elif self.consumable == "air":
            actual_usage_values = UsRsWeeklyConsumableGasSummary.objects.filter(
                date__range=[start_date, end_date]
            ).values()
        else:
            consumable_cat = RatesDefinition.objects.get(
                affected_consumable__istartswith=self.consumable
            )
            actual_usage_values = InventoryMgmtSystemConsumables.objects.filter(
                category_id=consumable_cat.category,
                datedim__range=[self.aware_min_date, self.aware_max_date],
            ).values(
                "datedim", "ims_id", "quantity", "status", "category", "category_name"
            )

        usage_df: pd.DataFrame | None = None

        if len(actual_usage_values) > 0:
            usage_df = pd.DataFrame(actual_usage_values)

        if usage_df is not None:
            if self.consumable == "water":
                usage_df = usage_df.drop(
                    columns=[
                        "corrected_potable_l",
                        "corrected_technical_l",
                        "resupply_potable_l",
                        "resupply_technical_l",
                    ]
                )
                usage_df = usage_df.rename(
                    columns={
                        "corrected_total_l": "actual_value",
                        "corrected_predicted_l": "predicted_value",
                    }
                )
            elif self.consumable == "oxygen":
                usage_df = usage_df.drop(
                    columns=[
                        "usos_o2_kg",
                        "rs_o2_kg",
                        "us_n2_kg",
                        "rs_n2_kg",
                        "adjusted_n2_kg",
                        "resupply_n2_kg",
                        "resupply_o2_kg",
                        "resupply_air_kg",
                    ]
                )
                usage_df = usage_df.rename(
                    columns={
                        "adjusted_o2_kg": "actual_value",
                    }
                )
                usage_df["predicted_value"] = None
            elif self.consumable == "nitrogen":
                usage_df = usage_df.drop(
                    columns=[
                        "usos_o2_kg",
                        "rs_o2_kg",
                        "us_n2_kg",
                        "rs_n2_kg",
                        "adjusted_o2_kg",
                        "resupply_n2_kg",
                        "resupply_o2_kg",
                        "resupply_air_kg",
                    ]
                )
                usage_df = usage_df.rename(columns={"adjusted_n2_kg": "actual_value"})
                usage_df["predicted_value"] = None
            elif self.consumable == "air":
                usage_df["actual_value"] = (
                    (usage_df["adjusted_n2_kg"] * 0.8)
                    + (usage_df["adjusted_o2_kg"] * 0.2)
                    + (usage_df["resupply_air_kg"].fillna(0))
                )
                usage_df = usage_df.drop(
                    columns=[
                        "usos_o2_kg",
                        "rs_o2_kg",
                        "us_n2_kg",
                        "rs_n2_kg",
                        "adjusted_o2_kg",
                        "adjusted_n2_kg",
                        "resupply_n2_kg",
                        "resupply_o2_kg",
                        "resupply_air_kg",
                    ]
                )
                usage_df["predicted_value"] = None
            else:
                usage_df = self.derive_ims_df(usage_df)

            return usage_df

    def derive_ims_df(self, df):
        # consumable = self.consumable.lower()
        # ims_qs = (
        #     InventoryMgmtSystemConsumables.objects
        #         ,annotate(date_only=Cast)
        #         .filter(category_name=consumable, datedim__range=[self.min_date, self.max_date])
        #         .values('datedim', 'category_name', 'quantity')
        #
        # )

        df = df[df["status"] != "Discard"]
        df = df[df["status"] != "Return"]
        df = df[df["status"] != np.nan]
        df["datedim"] = df["datedim"].dt.date

        unique = df.drop_duplicates(
            subset=["ims_id", "datedim", "status", "category_name"]
        )

        group_one = (
            unique.groupby(["datedim", "ims_id", "category_name"])
            .size()
            .reset_index(name="actual_value")
        )

        # print(group_one)

        grouped_df = (
            group_one.groupby(["datedim", "category_name"])
            .agg({"actual_value": "sum"})
            .reset_index()
        )
        grouped_df["predicted_value"] = None
        grouped_df = grouped_df.rename(columns={"datedim": "date"})

        # grouped_df = groups.size()
        # print(grouped_df)
        return grouped_df

    def init_water_data(self):
        water_summary_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            date__range=[self.min_date, self.max_date]
        ).values()
        self.weekly_water_summary = pd.DataFrame.from_records(
            water_summary_qs, index="date"
        )
        pass

    def get_usage_difference(self):
        assumed = self.rate_assumed()
        actual = self.rate_actual()

        if assumed == actual:
            return 0
        if assumed is None:
            return 0
        try:
            difference = ((assumed - actual) / assumed) * 100
            print(f"difference: {difference}%")
            return difference
        except ZeroDivisionError:
            return float("inf")
