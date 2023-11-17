import io
import pandas as pd
import numpy as np
from django.core.exceptions import PermissionDenied, ValidationError
from django.shortcuts import redirect, render
from .models import Upload
from .forms import UploadForm
from .utils.data_dictionary import data_dictionary
from .utils.insert_model import insert_model
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
    form = UploadForm(request.POST, request.FILES)

    if form.is_valid():
        # 1. Validate the file
        # figure out how to do custom file validation here
        # Django docs recommend doing more than just checking
        # the file type and extension because those can be spoofed.
        # Of course, if we just use pandas df.read_csv() on the file
        # and get an error, we know it's not a valid csv anyway.
        file = request.FILES["file"]
        try:
            # Hold onto a dataframe of the file upload.
            df = pd.read_csv(io.StringIO(file.read().decode("utf-8")))
            # remove unnamed columns
            df = df.loc[:, ~df.columns.str.match("Unnamed")]
        except Exception:
            # TODO: Return a custom error template here?
            raise ValidationError(f"{file} is not valid")

        # 2. Save file to disk & file path to db
        form.save()

        # 3. Instantiate/persist models to db
        columns = np.asarray(df.columns.to_numpy())
        model_name = None
        table_name = None

        for key in data_dictionary.keys():
            dictionary_entry = data_dictionary[key]
            entry_columns = dictionary_entry["columns"]
            dictionary_columns_arr = np.asarray(entry_columns)
            matches = np.array_equal(columns, dictionary_columns_arr)

            if matches is True:
                model_name = dictionary_entry["model_name"]
                table_name = key

        if model_name is None:
            raise ValidationError("Your file did not match any known data types")

        # print(f"model: {model_name}")

        # print(df.to_dict(orient="records"))
        # for index, row in df.iterrows():
        # for idx, row in df.iterrows():
        # model_result = insert_model(model_name, columns, np_row_arr)
        # model_result = insert_model(model_name, df.to_dict(orient="records"))
        data_service.insert_df(model_name, table_name, df)

        return render(
            request,
            "pages/data/filedetail.html",
            {
                "upload": request.FILES["file"],
                "tabledata": df.to_html(index=False, na_rep="", max_rows=100),
            },
        )
