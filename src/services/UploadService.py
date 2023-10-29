import os
from typing import List
from emmett.orm import Database
from models.Upload import Upload
from utils.Result import Result


class UploadService:
    """
    Fields:
        storage_dir:  The directory to store files in
        accepted_filetypes =  Valid file extensions for this service
        db:  A database connection
    """

    storage_dir: str
    accepted_filetypes: List[str]
    db: Database

    def __init__(
        self, db: Database, storage_path: str, accepted_filetypes: List[str]
    ) -> None:
        self.db = db
        self.__init_storage_dir(storage_path)
        self.accepted_filetypes = accepted_filetypes
        pass

    def __init_storage_dir(self, storage_path):
        dir_exists = os.path.isdir(storage_path)
        if not dir_exists:
            os.mkdir(storage_path)
        self.storage_dir = storage_path

    def is_valid_filetype(self, ext: str):
        if len(self.accepted_filetypes) == 0:
            return True

        return ext in self.accepted_filetypes

    def does_file_exist(self, file_path: str) -> bool:
        # check if file already exists
        return os.path.isfile(file_path)

    async def get_all_uploads(self) -> Result:
        """
        Get all uploads
        """
        uploads = Upload.all().select()
        return {"ok": True, "value": uploads, "error": None}

    async def get_upload_by_id(self, id: int) -> Result:
        """
        Get a single upload by its id
        """
        upload_result = Upload.get(id=id)

        if upload_result["id"] is None:
            if upload_result["errors"] is not None:
                error = list(upload_result["errors"].keys())[0]
                return {"ok": False, "error": error, "value": None}
            else:
                return {"ok": True, "value": None, "error": None}
        return {"ok": True, "value": upload_result, "error": None}

    async def save_file(self, file) -> Result:
        ext = file.content_type.split("/", 1)[1]
        file_location = f"{self.storage_dir}/{file.filename}"

        if not self.is_valid_filetype(ext):
            return {
                "ok": False,
                "error": f"{ext} is not a valid file type",
                "value": None,
            }

        if self.does_file_exist(file_location):
            return {
                "ok": False,
                "error": f"File named {file.filename} already exists",
                "value": None,
            }

        await file.save(file_location)

        return {"ok": True, "value": file_location, "error": None}

    def delete_file(self, file_path) -> Result:
        try:
            os.remove(file_path)
            return {"ok": True, "value": None, "error": None}
        except FileNotFoundError:
            return {
                "ok": False,
                "error": f"No file to delete at {file_path}",
                "value": None,
            }

    async def create_upload(self, file) -> Result:
        file_save_result = await self.save_file(file)
        file_location = None

        if file_save_result:
            if file_save_result["ok"] is not True:
                return file_save_result
            else:
                file_location = file_save_result["value"]

        upload = Upload.create(file_name=file.filename, file_path=file_location)
        # print(f'upload: {upload}')

        if upload["id"] is None:  # we got an error!
            error_key = list(upload["errors"])[0]
            error = upload["errors"][error_key]
            return {"ok": False, "error": error, "value": None}

        return {
            "ok": True,
            "value": {
                "id": upload["id"],
                "file_name": file.filename,
                "file_location": file_location,
            },
            "error": None,
        }
