import pytest
from server import purchasePlaces, app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def club():
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


@pytest.fixture
def competition():
    return [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Future comp",
            "date": "2026-10-22 13:30:00",
            "numberOfPlaces": "20"
        }
    ]

def test_valid_date(client, club, competition, monkeypatch):
    monkeypatch.setattr('server.competitions', competition)
    monkeypatch.setattr('server.clubs', club)
    response = client.post("book/Spring%20Festival/Simply%20Lift")
    assert response.status_code != 200
    assert b"The method is not allowed for the requested URL." in response.data

def test_invalid_date(client, club, competition, monkeypatch):
    monkeypatch.setattr('server.competitions', competition)
    monkeypatch.setattr('server.clubs', club)
    response = client.get("book/Spring%20Festival/Simply%20Lift")
    assert response.status_code == 200
    assert b"Sorry, this competition is expired." in response.data
    assert int(competition[0]['numberOfPlaces']) == 25
    assert int(club[0]['points']) == 13
