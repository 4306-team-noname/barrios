from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("get_form/", views.get_form, name="get_form"),
]
