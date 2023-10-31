import pytest
import os
from app import app, db as _db
import requests
import uuid

os.environ["TEST"] = "1"
# test_file_path = "test_files"


@pytest.fixture
def test_file_path():
    return "tests/test_files"


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def logged_client():
    c = app.test_client()
    with c.get("/auth/login").context as ctx:
        c.post(
            "/auth/login",
            data={
                "email": "analyst@test.test",
                "password": "SuperSecret123!",
                "_csrf_token": list(ctx.session._csrf)[-1],
            },
            follow_redirects=True,
        )
    return c


@pytest.fixture(scope="module", autouse=True)
def prepare_db():
    with _db.connection():
        _db.commit()
    yield _db
    with _db.connection():
        _db.rollback()


@pytest.fixture
def db(prepare_db):
    prepared_db = prepare_db
    return prepared_db


@pytest.fixture
def clean_csv(test_file_path):
    with open(f"{test_file_path}/clean.csv", "rb") as f:
        file_content = f.read()
        return create_multipart(file_content, "clean_csv", "clean_csv.csv", "text/csv")


@pytest.fixture
def no_header_csv(test_file_path):
    with open(f"{test_file_path}/no_header.csv", "rb") as f:
        file_content = f.read()
        return create_multipart(
            file_content, "no_header_csv", "no_header_csv.csv", "text/csv"
        )


@pytest.fixture
def shifted_csv(test_file_path):
    with open(f"{test_file_path}/shifted.csv", "rb") as f:
        file_content = f.read()
        return create_multipart(
            file_content, "shifted_csv", "shifted_csv.csv", "text/csv"
        )


@pytest.fixture
def test_text_file(test_file_path):
    with open(f"{test_file_path}/test_text_file.txt", "rb") as f:
        file_content = f.read()
        return create_multipart(
            file_content, "test_text_file", "test_text_file.txt", "text/plain"
        )


def create_multipart(file_content, name, file_name, file_type):
    boundary = str(uuid.uuid4())
    payload = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{name}"; filename="{file_name}"\r\n'
        f"Content-Type: {file_type}\r\n"
        "\r\n"
        f"{file_content.decode('utf-8')}\r\n"
        f"--{boundary}--\r\n"
    )
    return payload


"""
{'file': <FileStorage: ims_consumables_category_lookup.csv (text/csv)}
"""
