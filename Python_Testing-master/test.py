import pytest
from server import app, loadCompetitions, purchasePlaces


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


@pytest.fixture
def competitions():
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



def test_more_than_12_places(client, clubs, competitions, monkeypatch):
    monkeypatch.setattr('server.competitions', competitions)
    monkeypatch.setattr('server.clubs', clubs)
    response = client.post(
        '/purchasePlaces', data={
            "competition": competitions[0]['name'],
            "club": clubs[0]['name'],
            "places": 13})
    assert response.status_code == 200
    assert b"Sorry, you cannot book less than one place and more than 12 places !" in response.data


def test_less_than_1_place(client, clubs, competitions, monkeypatch):
    monkeypatch.setattr('server.competitions', competitions)
    monkeypatch.setattr('server.clubs', clubs)
    response = client.post(
        '/purchasePlaces', data={
            "competition": competitions[0]['name'],
            "club": clubs[0]['name'],
            "places": 0})
    assert response.status_code == 200
    assert b"Sorry, you cannot book less than one place and more than 12 places !" in response.data


def test_10_places(client, clubs, competitions, monkeypatch):
    monkeypatch.setattr('server.competitions', competitions)
    monkeypatch.setattr('server.clubs', clubs)
    response = client.post(
        '/purchasePlaces', data={
            "competition": competitions[0]['name'],
            "club": clubs[0]['name'],
            "places": 10})
    assert response.status_code == 200
    assert b"Great-booking complete !" in response.data


def test_valid_points(client, clubs, competitions, monkeypatch):
    monkeypatch.setattr('server.competitions', competitions)
    monkeypatch.setattr('server.clubs', clubs)
    response = client.post(
        '/purchasePlaces', data={
            "competition": competitions[0]['name'],
            "club": clubs[0]['name'],
            "places": 5})
    assert response.status_code == 200
    assert b"Great-booking complete !" in response.data
    assert int(competitions[0]['numberOfPlaces']) == 20
    assert int(clubs[0]['points']) == 8


def test_too_many_points(client, clubs, competitions, monkeypatch):
    monkeypatch.setattr('server.competitions', competitions)
    monkeypatch.setattr('server.clubs', clubs)
    response = client.post(
        '/purchasePlaces', data={
            "competition": competitions[0]['name'],
            "club": clubs[1]['name'],
            "places": 50})
    assert response.status_code == 200
    assert b'Sorry, you do not have the number of available places required to book this number of places.' in response.data
    assert b'Number of Places: 25' in response.data
    assert int(competitions[0]['numberOfPlaces']) == 25
    assert int(clubs[1]['points']) == 4