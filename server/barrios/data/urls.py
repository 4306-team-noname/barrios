from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:slug>/", views.data_detail, name="data_detail"),
    path("files/upload/", views.upload_post, name="upload_post"),
    # Keep these file urls just in case we decide there's a good
    # use for users viewing the files they uploaded.
    # path("files/", views.files, name="files"),
    # path("files/<int:id>/", views.file_detail, name="file_detail"),
]
