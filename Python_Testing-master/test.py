import pytest
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_known_email(client):
    """
    Given: A user access show summary
    When: he input a known email
    Then: we receive a status_code 200
    """
    email = "john@simplylift.co"
    response = client.post('/showSummary', data={"email": email})
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data


def test_unknown_email(client):
    """
    Given: A user access show summary
    When: he input an unknown email
    Then: we receive an error message
    """
    email = "johndoe@simplylift.co"
    response = client.post('/showSummary', data={"email": email})
    assert b"Sorry, that email was not found." in response.data
