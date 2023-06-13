import pytest
from server import purchasePlaces, app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def clubs():
    return [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {"name": "She Lifts",
         "email": "kate@shelifts.co.uk",
         "points": "12"
         }
    ]

def test_board_display(client,clubs,monkeypatch):
    """
    Given: A user access the site
    When: he access the index url
    Then: a list of clubs and their points is displayed
    """
    monkeypatch.setattr('server.clubs', clubs)
    response = client.get('/boardpoints')
    assert response.status_code == 200
    assert b"Table of Clubs Points" in response.data