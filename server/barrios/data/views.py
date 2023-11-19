import pandas as pd
import numpy as np
from pandas.compat import os
from csv import DictReader
from django.db import transaction
from django.core.exceptions import PermissionDenied, ValidationError
from django.shortcuts import redirect, render

from barrios.settings import MEDIA_ROOT
from .models import Upload
from .forms import UploadForm
from .utils.data_dictionary import data_dictionary

from .services import DataService


def index(request):
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


@transaction.atomic
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

    data_service = DataService()
    # NOTE: Maybe, instead of using the upload form here in
    # the view, it's better to use it in the service. It might
    # be easier to do everything in a transaction that way.
    form = UploadForm(request.POST, request.FILES)

    if form.is_valid():
        # TODO: Validate the file
        # figure out how to do custom file validation here
        # Django docs recommend doing more than just checking
        # the file type and extension because those can be spoofed.
        # Of course, if we just use pandas df.read_csv() on the file
        # and get an error, we know it's not a valid csv anyway.
        file = request.FILES["file"]

        # 2. Save file to disk & file path to db
        # TODO: Implement file saving and record insertion
        # as part of a transaction so everything can be rolled
        # back on failure
        result = form.save()
        filepath = os.path.join(MEDIA_ROOT, str(result.file))

        # 3. Instantiate/persist models to db
        col_df = pd.read_csv(filepath, nrows=0)
        col_df = col_df.loc[:, ~col_df.columns.str.match("Unnamed")]
        col_df = col_df.columns.tolist()
        columns = np.asarray(col_df)
        model_name = None
        table_name = None

        for key in data_dictionary.keys():
            dictionary_entry = data_dictionary[key]
            entry_columns = dictionary_entry["columns"]
            dictionary_columns_arr = np.asarray(list(entry_columns.keys()))
            matches = np.array_equal(columns, dictionary_columns_arr)

            if matches is True:
                model_name = dictionary_entry["model_name"]
                table_name = key

        if model_name is None:
            raise ValidationError("Your file did not match any known data types")
        # df = pd.read_csv(filepath)
        # df = df.loc[:, ~df.columns.str.match("Unnamed")]

        insert_result = data_service.read_and_insert_csv(model_name, filepath)
        if insert_result["ok"]:
            column_names = list(insert_result["value"][0].keys())
            fields = []
            for d in insert_result["value"]:
                fields.append(d.values())
            return render(
                request,
                "pages/data/filedetail.html",
                {
                    "file": file,
                    # "tabledata": df.to_html(index=false, na_rep="", max_rows=100),
                    "column_names": column_names,
                    "fields": fields,
                },
            )
        # else:
        # return an error template here


def file_detail(request, id):
    upload = Upload.objects.get(id=id)
    csv_path = os.path.join(MEDIA_ROOT, str(upload.file))
    with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
        print(file.name.split("/")[-1])
        reader = DictReader(file)
        fields = []
        column_names = []
        for row in reader:
            fields.append(list(row.values()))
            column_names = list(row.keys())

    return render(
        request,
        "pages/data/filedetail.html",
        {
            "filename": file.name.split("/")[-1],
            "column_names": column_names,
            "fields": fields,
        },
    )
