def test_db_exists(db):
    assert db is not None


def test_dashboard_page_works(client):
    rv = client.get("/")
    assert "Dashboard" in rv.data


def test_usage_page_works(client):
    rv = client.get("/usage")
    assert "Usage" in rv.data


def test_forecast_page_works(client):
    rv = client.get("/forecast")
    assert "Forecast" in rv.data


def test_flightplan_page_works(client):
    rv = client.get("/flightplan")
    assert "Flight Plan" in rv.data
