from math import ceil, floor
from random import randint
import pandas as pd
from django.db.models import Q
from data.models import (
    IssFlightPlan,
    ThresholdsLimitsDefinition,
    UsWeeklyConsumableWaterSummary,
)
from common.consumable_helpers import get_consumable_thresholds
from common.forms import AnalysisForm
import pandas as pd
from prophet import Prophet
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def create_forecast(consumable_name, min_date, max_date):
    consumable = consumable_name.lower()

    # if consumable == "water":
    if consumable:
        water_obj_qs = UsWeeklyConsumableWaterSummary.objects.filter(
            date__range=[min_date, max_date]
        ).values()
        df = pd.DataFrame.from_records(water_obj_qs)
        df["date"] = pd.to_datetime(df["date"])
        prophet_data = df[["date", "corrected_total_l"]].rename(
            columns={"date": "ds", "corrected_total_l": "y"}
        )  # type: ignore

        split_index = int(len(prophet_data) * 0.3)
        train_data = prophet_data[split_index:]
        test_data = prophet_data[:split_index]

        model = Prophet(
            yearly_seasonality=False,  # type: ignore
            weekly_seasonality=False,  # type: ignore
            daily_seasonality=True,  # type: ignore
            seasonality_mode="multiplicative",
            changepoint_prior_scale=0.05,
        )
        model.fit(train_data)

        future = model.make_future_dataframe(periods=365)
        forecast = model.predict(future)

        return {"model": model, "forecast": forecast}
