from server import app
from tests.mocks import mocker_clubs, mocker_competitions
from tests.fixture import client



def test_showSummary_valid_email(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    email = 'club2@test.com'
    response = client.post('/showSummary', data={'email' : email})
    assert response.status_code == 200
    assert b'Summary' in response.data
    assert b'club2@test.com' in response.data
    assert b'Competition 1' in response.data

def test_showSummary_unknown_email(mocker, client):
    mocker_clubs(mocker)
    email = 'unknown@test.com'
    response = client.post('/showSummary', data={'email' : email})
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
    assert b"Sorry this email doesn&#39;t exist in the club list" in response.data

