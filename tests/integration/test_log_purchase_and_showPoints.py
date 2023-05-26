from flask import request
from server import app
from tests.mocks import mocker_clubs, mocker_competitions
from tests.fixture import client


def test_log_and_logout(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    email = 'club1@test.com'
    response = client.post('/showSummary', data={'email' : email})
    assert response.status_code == 200
    assert b'Summary' in response.data
    with app.app_context():
        with client:
            response_2 = client.get('logout', follow_redirects=True)
            assert request.path == "/"
            assert response_2.status_code == 200
            assert b'Welcome to the GUDLFT Registration Portal!' in response_2.data

def test_log_purchase_and_logout(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    email = 'club1@test.com'
    response = client.post('/showSummary', data={'email' : email})
    assert response.status_code == 200
    assert b'Summary' in response.data
    assert b'club1@test.com' in response.data
    assert b'Competition 1' in response.data
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 1',
        'places': '2'
        }
    response_2 = client.post('/purchasePlaces', data = credentials)
    assert response_2.status_code == 200
    assert b'Great-booking complete!' in response_2.data
    assert b'Points available: 14' in response_2.data
    with app.app_context():
        with client:
            response_3 = client.get('logout', follow_redirects=True)
            assert request.path == "/"
            assert response_3.status_code == 200
            assert b'Welcome to the GUDLFT Registration Portal!' in response_3.data

def test_log_purchase_and_showPoints(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    email = 'club1@test.com'
    response = client.post('/showSummary', data={'email' : email})
    assert response.status_code == 200
    assert b'Summary' in response.data
    assert b'club1@test.com' in response.data
    assert b'Competition 1' in response.data
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 1',
        'places': '2'
        }
    response_2 = client.post('/purchasePlaces', data = credentials)
    assert response_2.status_code == 200
    assert b'Great-booking complete!' in response_2.data
    assert b'Points available: 14' in response_2.data
    with app.app_context():
        with client:
            response_3 = client.get('points', follow_redirects=True)
            assert request.path == "/points"
            assert response_3.status_code == 200
            assert b'Clubs Points' in response_3.data
            assert b'<td>14</td>' in response_3.data
