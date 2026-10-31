import pytest

from app import create_app
from data.resources import get_resources


@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    return app.test_client()


@pytest.mark.parametrize("path", ["/", "/about", "/tech", "/fitness"])
def test_main_pages_return_success(client, path):
    response = client.get(path)
    assert response.status_code == 200


def test_valid_resource_returns_success(client):
    response = client.get("/tech/python-programming")
    assert response.status_code == 200
    assert b"Python Programming" in response.data
    assert b"Open Google Drive materials" in response.data


def test_invalid_resource_returns_not_found(client):
    assert client.get("/tech/not-a-resource").status_code == 404


def test_unknown_route_returns_not_found(client):
    assert client.get("/does-not-exist").status_code == 404


def test_resources_load_from_json():
    resources = get_resources()
    assert len(resources) >= 9
    assert all(resource["slug"] for resource in resources)
