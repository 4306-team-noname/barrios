from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:consumable_name>/", views.get_forecast, name="get_forecast"),
]
