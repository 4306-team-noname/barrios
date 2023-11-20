import numpy as np
from pandas.compat import os
from pandas import DataFrame
from csv import DictReader
from django.db import transaction
from django.core.exceptions import PermissionDenied, ValidationError
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.core.paginator import Paginator
import django_tables2 as tables
from barrios.settings import MEDIA_ROOT
from .models import Upload
from .models.mappings import mappings
from .forms import UploadForm
from .utils.data_dictionary import data_dictionary
from .utils.FieldFileCsvHelper import FieldFileCsvHelper
from .services import DataService


def index(request):
    # TODO: This can just be a dumb view with a list
    # of links to a detail view for each user-data model
    if request.user.is_authenticated:
        data_service = DataService()
        uploads_queryset = Upload.objects.all()
        uploads = []

        for upload in uploads_queryset:
            upload_dict = {
                "name": str(upload.file).split("/")[1],
                "id": upload.id,
                "upload_date": upload.upload_date,
            }
            uploads.append(upload_dict)

        data = [
            {
                "name": "IMS Consumables",
                "ref": "ims_consumables",
                "count": data_service.get_count_by_ref("ims_consumables"),
            },
            {
                "name": "Category Lookup",
                "ref": "category_lookup",
                "count": data_service.get_count_by_ref("category_lookup"),
            },
            {
                "name": "Flight Plan",
                "ref": "flight_plan",
                "count": data_service.get_count_by_ref("flight_plan"),
            },
            {
                "name": "Crew Flight Plan",
                "ref": "crew_flight_plan",
                "count": data_service.get_count_by_ref("crew_flight_plan"),
            },
            {
                "name": "Crew Nationalities",
                "ref": "crew_nationality_lookup",
                "count": data_service.get_count_by_ref("crew_nationality_lookup"),
            },
            {
                "name": "US Water Summary",
                "ref": "us_water_summary",
                "count": data_service.get_count_by_ref("us_water_summary"),
            },
            {
                "name": "RSA Water Summary",
                "ref": "rsa_water_summary",
                "count": data_service.get_count_by_ref("rsa_water_summary"),
            },
            {
                "name": "Weekly Gas Summary",
                "ref": "weekly_gas_summary",
                "count": data_service.get_count_by_ref("weekly_gas_summary"),
            },
            {
                "name": "Rates Definitions",
                "ref": "rates_definitions",
                "count": data_service.get_count_by_ref("rates_definitions"),
            },
            {
                "name": "Tank Capacities",
                "ref": "tank_capacities",
                "count": data_service.get_count_by_ref("tank_capacities"),
            },
            {
                "name": "Thresholds and Limits",
                "ref": "thresholds_and_limits",
                "count": data_service.get_count_by_ref("thresholds_and_limits"),
            },
        ]
        context = {"data": data, "uploads": uploads}
        return render(request, "pages/data/data_list.html", context)
    else:
        return redirect("/accounts/login")


def data_detail(request, ref):
    data_service = DataService()
    result = data_service.get_data_by_ref(ref)
    if result["ok"]:
        data = result["value"]

        return render(request, "pages/data/data_detail.html", {"data": data})
    else:
        return redirect("/data/")


# @transaction.atomic
def upload_post(request):
    """
    Notes:
        - use <ClassName>._meta.db_table to get table name?
        - may still need a lookup dict to match cols to models
    """
    if request.method != "POST":
        # redirect to /data/ if not a POST request
        return redirect("/data/")

    if not request.user.is_authenticated:
        # send error if not authenticated
        # TODO: Implement a middleware to display a custom
        # template for this error
        raise PermissionDenied()

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

        for key in data_dictionary.keys():
            dictionary_entry = data_dictionary[key]
            dictionary_fieldnames_arr = np.asarray(
                list(dictionary_entry["columns"].keys())
            )
            matches = np.array_equal(fieldnames_arr, dictionary_fieldnames_arr)

            if matches is True:
                model_name = dictionary_entry["model_name"]
                new_fields = list(mappings[model_name].keys())

        if model_name is None:
            raise ValidationError("Your file did not match any known data types")
        else:
            if new_fields is not None:
                FieldFileCsvHelper().rewrite_csv(filepath, new_fields)
                insert_result = data_service.insert_csv(model_name)
                print(insert_result)
                if insert_result["ok"]:
                    return redirect(
                        f"/data/files/{upload_result.pk}",
                    )
                else:
                    os.remove(filepath)
                    return redirect("/data/")


def files(request):
    if request.user.is_authenticated:
        uploads_queryset = Upload.objects.all()
        uploads_count = uploads_queryset.count()
        uploads = []

        for upload in uploads_queryset:
            upload_dict = {
                "name": str(upload.file).split("/")[1],
                "id": upload.id,
                "upload_date": upload.upload_date,
            }
            uploads.append(upload_dict)

        context = {"uploads": uploads}

        # NOTE: We may be able to simplify this by just
        # sending the list of uploads and the form without
        # checking the upload count. If the template conditionally
        # renders what it needs to depending on uploads length.
        if uploads_count == 0:
            return render(request, "pages/data/index.html", context)
        else:
            return render(request, "pages/data/filelist.html", context)
    else:
        return redirect("/accounts/login")


def file_detail(request, id):
    upload = Upload.objects.get(id=id)
    file = upload.file
    csv_path = os.path.join(MEDIA_ROOT, str(upload.file))
    df: DataFrame = DataService().get_uploaded_file(csv_path)
    column_names = df.columns.tolist()
    rows = df.values.tolist()

    paginator = Paginator(rows, 100)

    page_num = request.GET.get("page")
    print(request.GET.get("page"))
    if not page_num:
        page_num = 1
    page_obj = paginator.get_page(page_num)

    return render(
        request,
        "pages/data/filedetail.html",
        {
            "filename": file.name.split("/")[-1],
            "column_names": column_names,
            # "fields": fields,
            "page_obj": page_obj,
        },
    )
