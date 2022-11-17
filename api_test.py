import pytest
from api import app

@pytest.fixture()
def app():
    app = app()

    app.config.update({
    "TESTING": True,
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def test_request(client):
    response = client.get('/origin')