from typing import List
from emmett.testing.helpers import BytesIO
import pytest
from modules.userdata.UploadService import UploadService
from emmett.orm import Database


@pytest.fixture(scope="function")
def upload_service(db, tmp_path):
    us = UploadService(db, tmp_path, ["csv"])
    return us


def test_upload_service_has_db(upload_service):
    assert isinstance(upload_service.db, Database)


def test_upload_service_has_storage_path(upload_service):
    assert upload_service.storage_dir is not None


def test_upload_service_has_accepted_files_list(upload_service):
    assert isinstance(upload_service.accepted_filetypes, List)


def test_saves_clean_csv_file(logged_client, clean_csv):
    # data = {"filename": "clean_csv.csv", "name": "", "headers": [], BytesIO(str.encode(clean_csv))}
    res = logged_client.post("/userdata/upload", data={"files": [clean_csv]})
    assert res.status == 200
