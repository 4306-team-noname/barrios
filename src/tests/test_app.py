def test_db_exists(db):
    assert db is not None


# Basic route status code tests


def test_dashboard_page_redirects_when_not_logged_in(client):
    res = client.get("/dashboard")
    assert res.status == 303


def test_dashboard_page_works_when_logged_in(logged_client):
    res = logged_client.get("/dashboard")
    assert res.status == 200


def test_usage_page_redirects_when_not_logged_in(client):
    res = client.get("/usage")
    assert res.status == 303


def test_usage_page_works_when_logged_in(logged_client):
    res = logged_client.get("/usage")
    assert res.status == 200


def test_forecast_page_redirects_when_not_logged_in(client):
    res = client.get("/forecast")
    assert res.status == 303


def test_forecast_page_works_when_logged_in(logged_client):
    res = logged_client.get("/forecast")
    assert res.status == 200


def test_flightplan_page_redirects_when_not_logged_in(client):
    res = client.get("/flightplan")
    assert res.status == 303


def test_flightplan_page_works_when_logged_in(logged_client):
    res = logged_client.get("/flightplan")
    assert res.status == 200


def test_userdata_page_redirects_when_not_logged_in(client):
    res = client.get("/userdata")
    assert res.status == 303


def test_userdata_page_works_when_logged_in(logged_client):
    res = logged_client.get("/userdata")
    assert res.status == 200
