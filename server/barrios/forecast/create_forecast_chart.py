import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
from math import floor


def create_forecast_chart(model, forecast, consumable_name=None, with_title=True):
    from prophet.plot import plot_plotly, plot_components_plotly

    fig = plot_plotly(model, forecast)

    # threshold_value = forecast_obj["threshold_value"]
    # threshold_plus_value = forecast_obj["threshold_plus_value"]
    # critical_value = forecast_obj["critical_value"]
    # min_value = forecast_obj["min_value"]
    # max_value = forecast_obj["max_value"]
    #
    # fig = go.Figure()
    # should_draw_lower_threshold = (threshold_plus_value - min_value) > 1
    # should_draw_upper_threshold = (max_value - threshold_plus_value) > 1
    # if should_draw_lower_threshold and should_draw_upper_threshold:
    #     # threshold+10% line
    #     fig.add_hline(
    #         y=threshold_plus_value,
    #         line_width=1,
    #         line_color="#ff0fff",
    #         line_dash="dot",
    #         opacity=0.8,
    #         annotation_text="Threshold + 10%",
    #         annotation_position="bottom right",
    #     )
    #     # threshold+10% -> threshold coloring
    #     fig.add_hrect(
    #         threshold_value,
    #         threshold_plus_value,
    #         line_width=0,
    #         fillcolor="#FF00FF",
    #         opacity=0.1,
    #         annotation_text="Threshold + 10%",
    #         annotation_position="top right",
    #     )
    # if critical_value:
    #     fig.add_hline(
    #         y=critical_value,
    #         line_width=3,
    #         line_color="red",
    #         line_dash="dot",
    #         opacity=0.9,
    #         annotation_text="Critical Level",
    #         annotation_position="bottom right",
    #     )
    # # below threshold coloring
    # fig.add_hrect(
    #     floor(threshold_value * 0.9),
    #     threshold_value,
    #     line_width=0,
    #     fillcolor="#FF00FF",
    #     opacity=0.3,
    # )
    # # threshold line
    # fig.add_hline(
    #     y=threshold_value,
    #     line_width=2,
    #     opacity=0.8,
    #     line_color="#FF00FF",
    #     line_dash="dot",
    #     annotation_text="Threshold",
    #     annotation_position="bottom right",
    # )
    #
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
    #
    # if with_title:
    #     fig.update_layout(title={"text": consumable_name.upper()})
    #
    # fig.add_trace(
    #     go.Scatter(
    #         x=list(df["date"]),
    #         y=list(df[consumable_name]),
    #         name=consumable_name,
    #         line=dict(color="#dade35", width=2),
    #     )
    # )
    chart = fig.to_html(
        config={"displayModeBar": False, "responsive": True},
        full_html=False,
        # default_height=600,
        # include_plotlyjs=False,
        include_mathjax=False,
    )
    return chart
