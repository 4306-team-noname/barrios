import pandas as pd
from pandas import DataFrame, Series
import plotly.graph_objs as go
import plotly.express as px
import datetime as dt
from typing import Any
import math
from django.db.models import Sum
from data.models import (
    IssFlightPlan,
    IssFlightPlanCrew,
    IssFlightPlanCrewNationalityLookup,
    RatesDefinition,
)


class Optimizer:
    consumable: str
    flight_plan: DataFrame
    crew_flight_plan: DataFrame
    rates_definition: DataFrame
    event_type: str
    event_dates: list[dt.date]
    event_vehicles: list[str]
    event_deltas: list[int]
    event_count: int
    crew_per_event: list[int]
    usos_crew_per_event: list[int]
    rsos_crew_per_event: list[int]
    commercial_crew_per_event: list[int]
    other_crew_per_event: list[int]

    def __init__(
        self, consumable: str, event_type="Launch", min_date=dt.date.today()
    ) -> None:
        self.consumable = consumable
        self.event_type = event_type
        fp_queryset = IssFlightPlan.objects.filter(datedim__gte=min_date).values()
        self.flight_plan = pd.DataFrame.from_records(fp_queryset, index="id")
        cfp_queryset = IssFlightPlanCrew.objects.filter(datedim__gte=min_date).values()
        self.crew_flight_plan = pd.DataFrame.from_records(cfp_queryset, index="id")
        rd_queryset = RatesDefinition.objects.all().values()
        self.rates_definition = pd.DataFrame.from_records(rd_queryset, index="id")
        self.crew_per_event = []
        self.usos_crew_per_event = []
        self.rsos_crew_per_event = []
        self.commercial_crew_per_event = []
        self.other_crew_per_event = []
        self.init_flightplan_data()
        self.init_crew_data()
        pass

    def run_optimization(self):
        launch_dates = self.event_dates
        vehicle_names = self.event_dates
        optimized_amounts = self.consumable_ascension()

        return {
            "date": launch_dates[:-1],
            "vehicle_names": self.event_vehicles[:-1],
            "amount": optimized_amounts,
        }

    def get_optimization_dataframe(self) -> DataFrame:
        optimization_object = self.run_optimization()
        optim_df = pd.DataFrame(optimization_object)
        return optim_df

    def plot(self):
        df = self.get_optimization_dataframe()
        # fig = go.Figure()
        fig = px.bar(df, x="date", y="amount")
        fig.update_traces(width=259_200_000, marker_color="#85a7e0")

        fig.update_layout(
            paper_bgcolor="#091D41",
            plot_bgcolor="#091D41",
            # title_font_color="#ffffff",
            legend_font_color="#ffffff",
            margin=dict(t=32, r=8, b=8, l=8),
            font=dict(color="#ffffff"),
            hovermode="x",
            newshape_layer="below",
            title=dict(
                text=self.consumable.upper(),
                automargin=False,
                font=dict(
                    size=22,
                    color="#ffffff",
                ),
            ),
        )

        fig.update_yaxes(
            showline=True,
            linewidth=1,
            linecolor="#5d7bb0",
            gridcolor="#5d7bb0",
        )
        bar_plot = fig.to_html(
            config={"displayModeBar": False, "responsive": True},
            full_html=False,
            default_height=600,
            # include_plotlyjs=False,
            include_mathjax=False,
        )
        return bar_plot

    def get_event_dates(self):
        return self.event_dates

    def get_event_vehicles(self):
        return self.event_vehicles

    def get_crew_counts(self):
        return {
            "usos_crew_per_event": self.usos_crew_per_event,
            "rsos_crew_per_event": self.rsos_crew_per_event,
            "other_crew_per_event": self.other_crew_per_event,
        }

    def init_flightplan_data(self) -> None:
        # Uses self.flight_plan to generate a list of event dates,
        # time deltas between those event dates, and a count of events

        # query to only use dates where the event is dock and convert it to a list
        self.event_dates = self.flight_plan[
            self.flight_plan["event"] == self.event_type
        ]["datedim"].tolist()

        # query to get the names of the vehicles associated
        # with self.event_type
        self.event_vehicles = self.flight_plan[
            self.flight_plan["event"] == self.event_type
        ]["vehicle_name"].tolist()

        # Create a list of the days difference between each date
        self.event_deltas = (
            pd.Series(self.event_dates).diff().dt.days.iloc[1:].astype(int).tolist()
        )

        # Get the number of events
        self.event_count = len(self.event_dates) - 1

    def init_crew_data(self) -> None:
        # Uses self.crew_flight_plan to generate a
        # list of the number of people on the space station
        for date in self.event_dates:
            usos_sum = 0
            rsos_sum = 0
            commercial_sum = 0
            other_sum = 0

            total_crew_num = IssFlightPlanCrew.objects.filter(datedim=date).aggregate(
                total=Sum("crew_count")
            )["total"]
            usos_nat_values = IssFlightPlanCrewNationalityLookup.objects.filter(
                is_usos_crew=True
            ).values("nationality")
            usos_nationalities = [n["nationality"].strip() for n in usos_nat_values]
            rsos_nat_values = IssFlightPlanCrewNationalityLookup.objects.filter(
                is_rsa_crew=True
            ).values("nationality")
            rsos_nationalities = [n["nationality"].strip() for n in rsos_nat_values]
            all_crew = IssFlightPlanCrew.objects.filter(datedim=date)

            for crew in all_crew:
                if crew.nationality_category in usos_nationalities:
                    usos_sum += crew.crew_count
                elif crew.nationality_category in rsos_nationalities:
                    rsos_sum += crew.crew_count
                elif crew.nationality_category == "Commercial":
                    commercial_sum += crew.crew_count
                else:
                    other_sum += crew.crew_count

            self.crew_per_event.append(total_crew_num)
            self.usos_crew_per_event.append(usos_sum)
            self.rsos_crew_per_event.append(rsos_sum)
            self.commercial_crew_per_event.append(commercial_sum)
            self.other_crew_per_event.append(other_sum)

    def rates(self, consumable):
        # wants the csv rates_definition, and a consumable
        rater = self.rates_definition
        # sum of generated
        sum_generated = sum(
            rater[
                (rater["affected_consumable"] == consumable)
                & (rater["type"] == "generation")
            ]["rate"].tolist()
        )

        # grabs the usage rates of consumable
        usage_list = rater[
            (rater["affected_consumable"] == consumable) & (rater["type"] == "usage")
        ]["rate"].tolist()

        # if units contains 'crew'
        crew_check = rater[
            (rater["affected_consumable"] == consumable) & (rater["type"] == "usage")
        ]["units"].tolist()

        sum_usage_list = []
        sum_usage_crew_list = []

        for i, j in enumerate(crew_check):
            if j.find("Crew") != -1:
                sum_usage_crew_list.append(usage_list[i])
            else:
                sum_usage_list.append(usage_list[i])

        sum_usage = sum(sum_usage_list)
        sum_usage_crew = sum(sum_usage_crew_list)

        return sum_usage, sum_usage_crew, sum_generated

    # idk yet
    def consumable_ascension(self) -> list[int]:
        df = self.event_deltas
        dock_days_list = self.event_dates
        num_days = self.event_count
        consumable = self.consumable

        sum_usage, sum_usage_crew, sum_generated = self.rates(consumable)
        # create a list of base rates
        listofrates = [sum_usage] * (num_days)
        listofrates_crew = []
        consumable_to_send = []
        current_sum = 0
        res_list = []

        for i in range(0, len(listofrates)):
            listofrates_crew.append(
                self.crew_per_event[i] * sum_usage_crew
                # get_crew_list(df, dock_days_list)[i] * sum_usage_crew
            )

        for i in range(0, len(listofrates)):
            res_list.append(
                ((listofrates[i] + listofrates_crew[i]) - sum_generated)
                * self.event_deltas[i]
            )

        # rounding
        for i, value in enumerate(res_list):
            current_sum += value
            consumable_to_send.append(math.trunc(current_sum))
            current_sum = current_sum - math.trunc(current_sum)

        # returns a list of the amount of consumables to send
        return consumable_to_send
