import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
from math import floor


def create_usage_chart(usage_obj, with_title=True):
    consumable_name = usage_obj["consumable_name"]
    df = usage_obj["df"]
    print(df)
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

    if with_title:
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
