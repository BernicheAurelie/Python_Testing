from tests.mocks import mocker_clubs, mocker_competitions, mocker_past_competitions
from tests.fixture import client


def test_purchase_12_places(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 4',
        'places': '12'
        }
    response = client.post('/purchasePlaces', data = credentials)
    assert response.status_code == 200
    assert b'Points available: 14' in response.data
    assert b'Great-booking complete!' in response.data

def test_purchase_more_than_12_places_forbidden(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 4',
        'places': '13'
        }
    response = client.post('/purchasePlaces', data = credentials)
    assert response.status_code == 200
    assert b'Points available: 50' in response.data
    assert b"Sorry, you can&#39;t book more than twelve places per competition" in response.data

def test_purchase_more_than_places_in_competition(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 3',
        'club': 'Club 1',
        'places': '11'
        }
    response = client.post('/purchasePlaces', data = credentials)
    assert response.status_code == 200
    assert b'Points available: 20' in response.data
    assert b"Sorry, there isn&#39;t enough places for the Competition 3" in response.data

def test_purchase_places_without_places_required(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 1',
        'places': ''
        }
    response = client.post('/purchasePlaces', data = credentials)
    assert response.status_code == 200
    assert b'Points available: 20' in response.data
    assert b"You have to specify how many places you want to book, please try again" in response.data
