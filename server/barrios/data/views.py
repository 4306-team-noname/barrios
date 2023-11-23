import numpy as np
from pandas.compat import os
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from barrios.settings import MEDIA_ROOT
from .models.mappings import mappings
from .forms import UploadForm
from .utils.data_dictionary import data_dictionary
from .utils.FieldFileCsvHelper import FieldFileCsvHelper
from .services import DataService


def index(request):
    # - Main view of the /data route -
    # This is basically a "dumb" view that
    # lists the different types of data enumerated
    # in the imported data_dictionary
    if request.user.is_authenticated:
        data_service = DataService()
        data = []

        # loop through the data_dictionary and build
        # the response data
        data = [
            {
                "name": data_dictionary[key]["readable_name"],
                "slug": data_dictionary[key]["slug"],
                "count": data_service.get_count_by_slug(data_dictionary[key]["slug"]),
            }
            for key in data_dictionary.keys()
        ]

        return render(request, "pages/data/data_list.html", {"data": data})
    else:
        # redirect if user is not authenticated
        return redirect("/accounts/login")


def data_detail(request, slug):
    # Detailed table view for a given type of
    # user data. This view requests the DataService
    # for stored data by the data type's "slug"
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
            return redirect("/data/")
    else:
        return redirect("/data/")


def upload_post(request):
    if not request.user.is_authenticated:
        # send error if not authenticated
        # TODO: Add error templates
        raise PermissionDenied()

    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    form = UploadForm(request.POST, request.FILES)

    if form.is_valid():
        upload_result = form.save()
        filename = str(upload_result.file)
        filepath = os.path.join(MEDIA_ROOT, filename)

        fieldnames = FieldFileCsvHelper().get_csv_header(filepath)
        fieldnames_arr = np.asarray(fieldnames)
        data_service = DataService(filepath)
        model_name = None
        new_fields = None
        slug = None

        for key in data_dictionary.keys():
            dictionary_entry = data_dictionary[key]
            dictionary_fieldnames_arr = np.asarray(
                list(dictionary_entry["columns"].keys())
            )
            matches = np.array_equal(fieldnames_arr, dictionary_fieldnames_arr)

            if matches is True:
                model_name = dictionary_entry["model_name"]
                new_fields = list(mappings[model_name].keys())
                slug = dictionary_entry["slug"]

        if model_name is None:
            # TODO: Send custom error template
            raise ValidationError("Your file did not match any known data types")
        else:
            if new_fields is not None:
                FieldFileCsvHelper().rewrite_csv(filepath, new_fields)
                insert_result = data_service.insert_csv(model_name)

                if insert_result["ok"]:
                    os.remove(filepath)
                    return redirect(
                        f"/data/{slug}",
                    )
                else:
                    os.remove(filepath)
                    return redirect("/data/")
