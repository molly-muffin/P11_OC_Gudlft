import pytest
from server import loadCompetitions, updatePlaces

def test_more_than_12_places():
    competitions = loadCompetitions()
    competition = competitions[0]
    placesRequired = 13
    response = updatePlaces(competition, placesRequired)
    assert not response

def test_less_than_1_place():
    competitions = loadCompetitions()
    competition = competitions[0]
    placesRequired = 0
    response = updatePlaces(competition, placesRequired)
    assert not response

def test_10_places():
    competitions = loadCompetitions()
    competition = competitions[0]
    placesRequired = 10
    response = updatePlaces(competition, placesRequired)
    assert response