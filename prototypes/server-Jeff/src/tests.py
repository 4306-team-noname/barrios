import pytest
from app import app


@pytest.fixture()
def client():
    return app.test_client()


def test_route_not_none(client):
    rv = client.get('/')
    assert rv is not None


def test_route_returns_dict_with_number(client):
    rv = client.get('/')
    print(rv)
    assert 'count' in rv.keys
