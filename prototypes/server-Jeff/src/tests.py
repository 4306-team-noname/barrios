import pytest
from app import app


@pytest.fixture()
def client():
    return app.test_client()


def test_route_not_none(client):
    rv = client.get('/')
    assert rv is not None
