import pytest
import os
from app import app, db as _db, User, auth
from emmett.orm.migrations.utils import generate_runtime_migration
from emmett.testing.helpers import filesdict


os.environ["TEST"] = "1"
test_file_path = "test_files"


@pytest.fixture
def test_file_path():
    return "test_files"


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture(scope="module", autouse=True)
def prepare_db():
    with _db.connection():
        migration = generate_runtime_migration(_db)
        migration.up()
    yield _db
    with _db.connection():
        User.all().delete()
        auth.delete_group("admin")
        migration.down()


@pytest.fixture
def db(prepare_db):
    prepared_db = prepare_db
    return prepared_db


@pytest.fixture(scope="session")
def clean_csv(test_file_path):
    test_file = os.path.join(test_file_path, "clean.csv")
    with open(test_file, "r+") as file:
        return file


@pytest.fixture(scope="session")
def no_header_csv(test_file_path):
    test_file = os.path.join(test_file_path, "no_header.csv")
    with open(test_file, "r+") as file:
        return file


@pytest.fixture(scope="session")
def shifted_data_csv(test_file_path):
    test_file = os.path.join(test_file_path, "shifted_data.csv")
    with open(test_file, "rb") as fh:
        buffer = BytesIO(fh.read())
        fs = FileStorage


"""
{'file': <FileStorage: ims_consumables_category_lookup.csv (text/csv)}
"""
