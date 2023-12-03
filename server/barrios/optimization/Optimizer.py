from typing import Any
import pandas as pd
from pandas import DataFrame, Series
import datetime as dt
import math
from data.models import IssFlightPlan, IssFlightPlanCrew, RatesDefinition


class Optimizer:
    consumable: str
    flight_plan: DataFrame
    crew_flight_plan: DataFrame
    rates_definition: DataFrame
    event_type: str
    event_dates: list[dt.date]
    event_deltas: list[int]
    event_count: int
    crew_per_event: list[int]

    def __init__(self, consumable: str, event_type="Launch") -> None:
        self.consumable = consumable
        self.event_type = event_type
        fp_queryset = IssFlightPlan.objects.all().values()
        self.flight_plan = pd.DataFrame.from_records(fp_queryset, index="id")
        cfp_queryset = IssFlightPlanCrew.objects.all().values()
        self.crew_flight_plan = pd.DataFrame.from_records(cfp_queryset, index="id")
        rd_queryset = RatesDefinition.objects.all().values()
        self.rates_definition = pd.DataFrame.from_records(rd_queryset, index="id")
        self.crew_per_event = []
        self.init_dates()
        self.init_crew_list()
        pass

    def init_dates(self) -> None:
        # Uses self.flight_plan to generate a list of event dates,
        # time deltas between those event dates, and a count of events

        # query to only use dates where the event is dock and convert it to a list
        self.event_dates = self.flight_plan[
            self.flight_plan["event"] == self.event_type
        ]["datedim"].tolist()

        # Create a list of the days difference between each date
        self.event_deltas = (
            pd.Series(self.event_dates).diff().dt.days.iloc[1:].astype(int).tolist()
        )

        # Get the number of events
        self.event_count = len(self.event_dates) - 1

    def init_crew_list(self) -> None:
        # Uses self.crew_flight_plan to generate a
        # list of the number of people on the space station
        for date in self.event_dates:
            crewNum = self.crew_flight_plan[self.crew_flight_plan["datedim"] == date][
                "crew_count"
            ].tolist()
            amount = sum(crewNum)
            self.crew_per_event.append(amount)

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
