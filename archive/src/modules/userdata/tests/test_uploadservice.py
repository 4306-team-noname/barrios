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


def test_saves_clean_csv_file(logged_client, test_file_path):
    with open(f"{test_file_path}/clean.csv", "rb") as clean_csv:
        data = {
            "filename": "clean_csv.csv",
            "name": "clean_csv",
            "file": clean_csv,
        }
        res = logged_client.post("/userdata/upload", data=data)
    assert res.status == 200


def test_rejects_text_file(logged_client, test_file_path):
    with open(f"{test_file_path}/test_text_file.txt", "rb") as text_file:
        data = {
            "filename": "test_text_file.txt",
            "name": "test_text_file",
            "file": text_file,
        }
        res = logged_client.post("/userdata/upload", data=data)
    assert res.status == 415
