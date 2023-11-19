from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.file_detail, name="file_detail"),
    path("upload/", views.upload_post, name="upload"),
]
