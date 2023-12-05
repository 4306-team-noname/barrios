from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("missions/", views.missions, name="missions"),
    path("consumables/", views.consumables, name="consumables"),
    path(
        "get_optimization/<str:consumable_name>/",
        views.get_optimization,
        name="get_optimization",
    ),
]
