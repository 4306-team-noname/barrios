from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "get_forecast/<str:consumable_name>/", views.get_forecast, name="get_forecast"
    ),
    path("analyze/", views.analyze, name="analyze"),
]
