from server import app
from tests.mocks import mocker_clubs, mocker_competitions
from tests.fixture import client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Welcome to the GUDLFT Registration Portal!' in response.data.decode() 

def test_logout_user(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data

def test_purchase_places(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    response = client.get('/book/Competition%201/Club%201')
    assert response.status_code == 200
    assert b'Booking for' in response.data
    assert b'Competition 1' in response.data
    assert b'Club 1' in response.data

def test_purchase_places_bad_url(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    response = client.get('/book/Competitionxxxxxx/Clubxxxxxxx')
    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
