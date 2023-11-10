import io
import pandas as pd
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models.Upload import Upload
from .forms import UploadFileForm


def index(request):
    all_uploads = Upload.objects.all()
    uploads_count = all_uploads.count()

    if uploads_count == 0:
        return render(request, "pages/data/index.html")
    else:
        return render(request, "pages/data/filelist.html")


@require_POST
def upload_post(request):
    """
    Notes:
        - use <ClassName>._meta.db_table to get table name?
        - may still need a lookup dict to match cols to models
    """
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        file = request.FILES["file"]
        try:
            df = pd.read_csv(io.StringIO(file.read().decode("utf-8")))
        except Exception:
            return None
        return render(
            request,
            "pages/data/filedetail.html",
            {
                "upload": request.FILES["file"],
                "tabledata": df.to_html(index=False, na_rep=""),
            },
        )
