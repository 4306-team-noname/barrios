from math import ceil, floor
from data.models import IssFlightPlan, ThresholdsLimitsDefinition
from random import randint, uniform
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go


def get_forecast_chart(consumable_name):
    docking_date_values = IssFlightPlan.objects.filter(event="Dock").values("datedim")
    docking_dates = [d["datedim"] for d in docking_date_values]

    threshold = list(
        ThresholdsLimitsDefinition.objects.filter(
            threshold_category=consumable_name
        ).values()
    )[0]

    threshold_value = threshold["threshold_value"] + threshold["threshold_value"] * 0.1
    max_val = int(ceil(threshold["threshold_value"] * 1.25))
    min_val = int(floor(threshold_value * 0.9))

    dummy_forecast = []
    for docking_date in docking_dates:
        forecast = {
            "date": docking_date,
            consumable_name: randint(min_val, max_val),
        }
        dummy_forecast.append(forecast)

    df = pd.DataFrame(dummy_forecast)

    fig = go.Figure()
    should_draw_lower_threshold = (threshold_value - min_val) > 1
    should_draw_upper_threshold = (max_val - threshold_value) > 1
    # fig = px.line(df, x="date", y=list(df.columns)[1:], color="#dade35")
    if should_draw_lower_threshold and should_draw_upper_threshold:
        fig.add_hline(
            y=threshold_value,
            line_width=1,
            line_color="#ff0fff",
            line_dash="dot",
            opacity=0.8,
            annotation_text="Threshold + 10%",
            annotation_position="bottom right",
        )
        fig.add_hrect(
            threshold["threshold_value"],
            threshold_value,
            line_width=0,
            fillcolor="#FF00FF",
            opacity=0.1,
            annotation_text="Threshold + 10%",
            annotation_position="top right",
        )
        fig.add_hrect(
            threshold["threshold_value"] * 0.9,
            threshold["threshold_value"],
            line_width=0,
            fillcolor="#FF00FF",
            opacity=0.3,
        )
    # threshold line
    fig.add_hline(
        y=threshold["threshold_value"],
        line_width=2,
        opacity=0.8,
        line_color="#FF00FF",
        line_dash="dot",
        annotation_text="Threshold",
        annotation_position="bottom right",
    )

    fig.update_layout(
        paper_bgcolor="#091D41",
        plot_bgcolor="#091D41",
        title_font_color="#ffffff",
        legend_font_color="#ffffff",
        margin=dict(t=4, r=4, b=4, l=4),
        font=dict(color="#ffffff"),
    )
    fig.add_trace(
        go.Scatter(
            x=docking_dates,
            y=list(df[consumable_name]),
            name=consumable_name,
            line=dict(color="#dade35", width=2),
        )
    )
    line_plot = plot(
        fig,
        output_type="div",
        config={"displayModeBar": False},
    )
    return line_plot
