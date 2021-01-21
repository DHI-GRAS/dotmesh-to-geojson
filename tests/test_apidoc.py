def test_check_swagger(flask_client):
    rv = flask_client.get("/swagger.json")

    assert rv.status_code == 200
    assert rv.json


def test_check_apidoc(flask_client):
    rv = flask_client.get("/apidoc")

    assert rv.status_code == 200
