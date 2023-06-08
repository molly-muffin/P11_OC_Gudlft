import pytest
from server import loadCompetitions, loadClubs, updatePlaces

def test_more_than_12_places():
    competitions = loadCompetitions()
    competition = competitions[0]
    placesRequired = 13
    return_value = updatePlaces(competition, placesRequired)
    assert not return_value


def test_less_than_1_place():
    competitions = loadCompetitions()
    competition = competitions[0]
    placesRequired = 0
    return_value = updatePlaces(competition, placesRequired)
    assert not return_value


def test_10_places():
    competitions = loadCompetitions()
    competition = competitions[0]
    placesRequired = 10
    return_value = updatePlaces(competition, placesRequired)
    assert return_value