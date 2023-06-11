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


def test_valid_points(client, club, competition, monkeypatch):
    monkeypatch.setattr('server.competitions', competition)
    monkeypatch.setattr('server.clubs', club)

    response = client.post(
        '/purchasePlaces', data={
            "competition": competition[0]['name'],
            "club": club[0]['name'],
            "places": 5})

    assert response.status_code == 200
    assert b"Great-booking complete !" in response.data
    assert int(competition[0]['numberOfPlaces']) == 20
    assert int(club[0]['points']) == 8

def test_too_many_points(client, club, competition, monkeypatch):
    monkeypatch.setattr('server.competitions', competition)
    monkeypatch.setattr('server.clubs', club)

    response = client.post(
        '/purchasePlaces', data={
            "competition": competition[0]['name'],
            "club": club[1]['name'],
            "places": 50})

    assert response.status_code == 200
    assert b'Sorry, you do not have the number of available places required to book this number of places.' in response.data
    assert b'Number of Places: 25' in response.data
    assert int(competition[0]['numberOfPlaces']) == 25
    assert int(club[1]['points']) == 4