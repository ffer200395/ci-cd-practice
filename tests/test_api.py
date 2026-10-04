from api.index import suma, app


def test_suma():
    assert suma(2, 3) == 5


def test_api():
    client = app.test_client()

    response = client.get("/api")

    assert response.status_code == 200
    assert response.json == {"result": 5}