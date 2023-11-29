import numpy as np
from pandas.compat import os
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django_htmx.http import HttpResponseClientRedirect
import json
from common.conditionalredirect import conditionalredirect
from core.settings import MEDIA_ROOT
from data.core.data_dictionary import data_dictionary
from data.core.FieldFileCsvHelper import FieldFileCsvHelper
from data.core.get_file_info import get_file_info
from data.services import DataService
from .forms import UploadForm


def index(request, context=None):
    # - Main view of the /data route -
    # This is basically a "dumb" view that
    # lists the different types of data enumerated
    # in the imported data_dictionary
    if not request.user.is_authenticated:
        # redirect if user is not authenticated
        return conditionalredirect(request, "/accounts/login/")

    missing_data = None
    if request.session.get("missing_data"):
        missing_data = request.session.get("missing_data")

    data_service = DataService()
    data = []

    # loop through the data_dictionary and build
    # the response data
    # TODO: Perhaps, set the data dictionary items
    # as model attributes instead
    data = [
        {
            "name": data_dictionary[key]["readable_name"],
            "slug": data_dictionary[key]["slug"],
            "count": data_service.get_count_by_slug(data_dictionary[key]["slug"]),
        }
        for key in data_dictionary.keys()
    ]

    return render(
        request,
        "pages/data/data_list.html",
        {"data": data, "current_page": "data", "missing_data": missing_data},
    )


def data_detail(request, slug):
    # Detailed table view for a given type of
    # user data.
    if not request.user.is_authenticated:
        return conditionalredirect(request, "/accounts/login/")

    data_service = DataService()

    result = data_service.get_data_by_slug(slug)

    if result["ok"]:
        if result["value"]:
            data = result["value"]["data"]
            name = result["value"]["name"]

            return render(
                request, "pages/data/data_detail.html", {"data": data, "name": name}
            )
        else:
            return conditionalredirect(request, "/data/")
    else:
        return conditionalredirect(request, "/data/")


def upload_post(request):
    if not request.user.is_authenticated:
        # send error if not authenticated
        # TODO: Add error templates
        raise PermissionDenied()

    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    form = UploadForm(request.POST, request.FILES)

    if form.is_valid():
        upload_object = form.save()
    else:
        return render("/data/", form)

    filename = str(upload_object.file)
    filepath = os.path.join(MEDIA_ROOT, filename)
    data_service = DataService(filepath)

    fileinfo_result = get_file_info(filepath)

    if not fileinfo_result["ok"]:
        # TODO: Send custom error template?
        raise ValidationError(fileinfo_result["error"])
    else:
        if fileinfo_result["value"]:
            fileinfo = fileinfo_result["value"]
            # ensure csv column names are rewritten to reflect
            # fields in db
            # TODO: Rewrite this function so that it checks whether the
            # given file's column names already match the table fields
            # associated with the file's model.
            FieldFileCsvHelper().rewrite_csv(filepath, fileinfo["db_fields"])
            insert_result = data_service.insert_csv(fileinfo["model_name"])
            if insert_result["ok"]:
                os.remove(filepath)
                return conditionalredirect(
                    request,
                    f"/data/{fileinfo[ 'slug' ]}/",
                )
            else:
                os.remove(filepath)
                return conditionalredirect(request, "/data/")
