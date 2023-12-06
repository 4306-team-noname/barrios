from typing import Dict
import numpy as np
from ortools.linear_solver import pywraplp
from common.consumable_helpers import (
    get_consumable_names,
    get_consumable_thresholds,
    get_consumable_units,
)
from common.flightplan_helpers import get_flightplan_dates, get_flightplan_deltas
from numpy.typing import ArrayLike
from usage.Rater import Rater


class OrOptimizer:
    consumable_names: ArrayLike
    consumables_required: ArrayLike
    consumable_mapping: Dict
    thresholds: ArrayLike
    usage_rates: ArrayLike
    launch_dates: ArrayLike
    solver: pywraplp.Solver

    def __init__(self) -> None:
        self.consumable_names = np.array(get_consumable_names())
        self.consumables_required = np.array(
            [[i for i in range(0, len(self.consumable_names))]]
        )
        self.consumable_mapping = {
            consumable: i for i, consumable in enumerate(self.consumable_names)
        }
        self.launch_dates = np.array(get_flightplan_dates(event_type="Launch"))
        self.solver = pywraplp.Solver.CreateSolver("GLOP")
        thresholds = []
        rates = []
        for consumable_name in self.consumable_names:
            threshold_value_object = get_consumable_thresholds(consumable_name)
            threshold_value = threshold_value_object["threshold_value"]
            thresholds.append(threshold_value)
            rater = Rater(consumable_name)
            actual_rate = rater.rate_actual()
            if actual_rate < 0:
                actual_rate = -actual_rate
            rates.append(actual_rate)
        self.thresholds = np.array(thresholds)
        self.usage_rates = np.array(rates)

    def optimize(self) -> None:
        print(self.usage_rates)
        num_launches = len(self.launch_dates)  # type: ignore
        num_consumables = len(self.consumables_required[0])  # type: ignore
        consumables = [
            [
                self.solver.NumVar(0, self.solver.infinity(), f"consumable_{i}_{j}")
                for j in range(num_consumables)
            ]
            for i in range(num_launches)
        ]

        # Objective function
        objective = self.solver.Objective()
        objective.SetMinimization()

        for i in range(num_launches):
            for j in range(num_consumables):
                objective.SetCoefficient(consumables[i][j], 1)

        # Constraints
        for i in range(num_consumables):
            constraint = self.solver.Constraint(
                self.thresholds[i],  # type: ignore
                self.solver.infinity(),
            )  # type: ignore
            for j in range(num_launches):
                constraint.SetCoefficient(consumables[j][i], -1)

        usage_rate_constraint = self.solver.Constraint(0, 0)
        for i in range(num_launches):
            for j in range(num_consumables):
                usage_rate_constraint.SetCoefficient(
                    consumables[i][j],
                    -self.usage_rates[j],  # type: ignore
                )

        # Solve
        self.solver.Solve()

        # Extract results
        consumables_per_launch = np.zeros((num_launches, num_consumables))
        for i in range(num_launches):
            for j in range(num_consumables):
                consumables_per_launch[i, j] = consumables[i][j].solution_value()

        # Print the results
        print("Optimal number of consumables in each launch:")
        print(consumables_per_launch)
        print("Total number of launches:", int(objective.Value()))
