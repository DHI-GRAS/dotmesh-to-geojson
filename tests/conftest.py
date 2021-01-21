import pytest


@pytest.fixture(scope="session")
def flask_app():
    from dotmeshgj.flask_api import create_app

    return create_app()


@pytest.fixture(scope="session")
def flask_client(flask_app):
    with flask_app.test_client() as client:
        yield client
