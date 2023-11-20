from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:ref>/", views.data_detail, name="data_detail"),
    path("files/upload/", views.upload_post, name="upload"),
    path("files/", views.files, name="files"),
    path("files/<int:id>/", views.file_detail, name="file_detail"),
]
