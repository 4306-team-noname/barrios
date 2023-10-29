from typing import List
import pytest
from services.UploadService import UploadService
from models.Upload import Upload
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


async def saves_file(upload_service, shifted_csv):
    print(await shifted_csv.files)
    assert False
