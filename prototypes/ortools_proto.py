import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp

fp_df = pd.read_csv("../iss-data/csv/iss_flight_plan_20220101-20251231.csv")

launch_dates_df = fp_df.loc[fp_df["event"] == "Launch"]
launch_dates_df = launch_dates_df.drop(
    ["port_name", "vehicle_type", "eva_name", "eva_type", "eva_accuracy", "event"],
    axis=1,
)

launch_dates = launch_dates_df["datedim"].to_numpy()
vehicle_names = launch_dates_df["vehicle_name"].to_numpy()

thresholds_df = pd.read_csv("../iss-data/csv/thresholds_limits_definition.csv")
thresholds_df = thresholds_df.loc[thresholds_df["threshold_owner"] != "RSOS"]
thresholds_df = thresholds_df.loc[
    thresholds_df["threshold_category"] != "Water Critical"
]

thresholds_df.loc[0, "threshold_category"] = "ACY Inserts"
thresholds_df.loc[11, "threshold_category"] = "Oxygen"
thresholds_df.loc[12, "threshold_category"] = "Nitrogen"
thresholds_df.loc[13, "threshold_category"] = "Water"
thresholds_df.loc[15, "threshold_category"] = "US Food BOBs"

units = thresholds_df["units"].tolist()
thresholds = thresholds_df["threshold_value"].to_numpy()

consumables_str = thresholds_df["threshold_category"].to_numpy()
consumable_id_mapping = {consumable: i for i, consumable in enumerate(consumables_str)}
consumables_required = np.array([list(consumable_id_mapping.values())])

# dummy rates
usage_rates = np.array(
    [
        3.9,
        0.107142738,
        0.016666668,
        0.22727274,
        0.22727274,
        0.22727274,
        5.49,
        0.484929,
        20.02,
        0.081,
    ]
)
launch_dates = np.array(launch_dates)

solver = pywraplp.Solver.CreateSolver("GLOP")
num_launches = len(launch_dates)
num_consumables = len(consumables_required[0])

consumables = [
    [
        solver.NumVar(0, solver.infinity(), f"consumable_{i}_{j}")
        for j in range(num_consumables)
    ]
    for i in range(num_launches)
]
objective = solver.Objective()
objective.SetMinimization()

for i in range(num_launches):
    for j in range(num_consumables):
        objective.SetCoefficient(consumables[i][j], 1)

for i in range(num_consumables):
    constraint = solver.Constraint(thresholds[i], solver.infinity())
    for j in range(num_launches):
        constraint.SetCoefficient(consumables[j][i], -1)

usage_rate_constraint = solver.Constraint(0, 0)
for i in range(num_launches):
    for j in range(num_consumables):
        usage_rate_constraint.SetCoefficient(consumables[i][j], -usage_rates[j])

solver.Solve()

consumables_per_launch = np.zeros((num_launches, num_consumables))

for i in range(num_launches):
    for j in range(num_consumables):
        consumables_per_launch[i, j] = consumables[i][j].solution_value()

print("Optimal number of consumables in each launch:")
print(consumables_per_launch)
print("Total number of launches:", int(objective.Value()))
