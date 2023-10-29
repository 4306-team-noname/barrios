from app import app, db
from typing import Final
from emmett import request, response, session
from emmett.helpers import flash

from services.UploadService import UploadService
from services.DataService import DataService
from utils.Result import Result

# Define data as an app module so routes can be nested within
data = app.module(
    __name__, "userdata", url_prefix="userdata", template_folder="pages/userdata"
)

storage_path: Final = "storage"  # TODO: set as environment variable?
upload_service = UploadService(db, storage_path, ["csv"])
data_service = DataService(db)


@data.route("/")
async def index():
    """
    This route retrieves a list of all the User's uploads and returns
    a list of links to view each one.
    TODO: Setup auth! Right now this route simply get all uploads.
    """
    response.meta.title = "Data | ISS Consumables"
    uploads_result = await upload_service.get_all_uploads()

    if uploads_result["ok"] is not True:
        return flash("There was an error getting the uploads", "error")

    uploads = uploads_result["value"]
    return {"uploads": uploads}


@data.route("/<int:id>")
async def file(id: int):
    """
    Returns all entries associated with an upload as an HTML table with
    a link to download the data as a CSV file
    """
    upload_result = await upload_service.get_upload_by_id(id)

    if upload_result["ok"] is False:
        response.meta.title = "Error | ISS Consumables"
        return flash("There was a problem retrieving the upload", "error")

    upload_data = upload_result["value"]

    return {"upload": upload_data}


@data.route("/upload", methods="post")
async def upload():
    """
    This route handles uploading a new file and persisting
    its data to a database
    TODO: Consider moving the upload & persistence logic
    into services (UploadService, UserDataService)
    response.meta.title = 'Upload | ISS Consumables'
    """

    files = await request.files
    print(f"files: {files}")
    file = files.file

    upload_result: Result = await upload_service.create_upload(file)

    if upload_result:
        if upload_result["ok"] is False:
            return flash("There was a problem uploading the file", "error")
        print(upload_result["value"])
        file_location = upload_result["value"]["file_location"]
    else:
        return flash("There was a problem uploading the file", "error")

    file_result = data_service.save_file_data(file_location)

    if file_result:
        if file_result["ok"] is not True:
            error = file_result["error"]
            print(f"File result error: {error}")
            return flash(error, "error")
        else:
            val = file_result["value"]
            table_cols = val["table_cols"]
            dataframe = val["dataframe"]
            table_list = val["table_list"]

        response.meta.title = f"upload_result['value']['file_name'] | ISS Consumables"
        # return an HTML table
        # (possibly paginated, in the case of thousands of rows)
        return {
            "name": upload_result["value"]["file_name"],
            "table_cols": table_cols,
            "dataframe": dataframe,
            "table_list": table_list,
        }
