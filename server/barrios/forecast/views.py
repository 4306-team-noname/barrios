from django.http import HttpResponse
from django.shortcuts import redirect, render
from common.conditionalredirect import conditionalredirect
from data.models import IssFlightPlan, ThresholdsLimitsDefinition
from random import randint, uniform
import pandas as pd
from plotly.offline import plot
import plotly.express as px


def index(request):
    if request.user.is_authenticated:
        return render(request, "pages/forecast/index.html")
    else:
        return conditionalredirect(request, "/accounts/login/")


def get_forecast(request, consumable_name):
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")
    docking_date_values = IssFlightPlan.objects.filter(event="Dock").values("datedim")
    docking_dates = [d["datedim"] for d in docking_date_values]

    threshold = list(
        ThresholdsLimitsDefinition.objects.filter(
            threshold_category=consumable_name
        ).values()
    )[0]

    threshold_value = threshold["threshold_value"] + threshold["threshold_value"] * 0.1
    max_val = threshold["threshold_value"] * 1.25
    min_val = threshold_value * 0.9

    dummy_forecast = []
    for docking_date in docking_dates:
        forecast = {"date": docking_date, consumable_name: uniform(min_val, max_val)}
        dummy_forecast.append(forecast)

    df = pd.DataFrame(dummy_forecast)
    fig = px.line(df, x="date", y=list(df.columns)[1:])
    fig.add_hline(y=threshold_value, line_width=1, line_color="#914538", opacity=1)
    fig.add_hline(
        y=threshold["threshold_value"],
        line_width=3,
        line_color="#782416",
        annotation_text="Threshold",
        annotation_position="bottom right",
    )
    fig.add_hrect(
        threshold["threshold_value"],
        threshold_value,
        line_width=0,
        fillcolor="#914538",
        opacity=0.4,
        annotation_text="Threshold + 10%",
        annotation_position="top right",
    )
    fig.add_hrect(
        threshold["threshold_value"] * 0.9,
        threshold["threshold_value"],
        line_width=0,
        fillcolor="#782416",
        opacity=0.4,
    )
    fig.update_layout(
        paper_bgcolor="#091D41",
        plot_bgcolor="#091D41",
        title_font_color="#ffffff",
        legend_font_color="#ffffff",
        margin=dict(t=4, r=4, b=4, l=4),
        font=dict(color="#ffffff"),
    )
    line_plot = plot(
        fig,
        output_type="div",
        config={"displayModeBar": False},
    )

    return render(
        request, "pages/forecast/forecast_plot.html", {"forecast_plot": line_plot}
    )

    print(threshold)
