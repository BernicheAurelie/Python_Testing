import server
from tests.mocks import mocker_clubs, mocker_competitions
from tests.fixture import client

def test_points_board_status_code_ok(client):
    response = client.get('/points')
    assert response.status_code == 200
    assert b'Clubs Points' in response.data

def test_points_board_bad_url(client):
    response = client.get('/board')
    assert response.status_code == 404

def test_showPoints(mocker, client):
    mocker_clubs(mocker)
    response = client.get('/points')
    assert b'Club 1' in response.data
    assert b'<td>20</td>' in response.data
    assert b'Club 2' in response.data
    assert b'<td>15</td>' in response.data

def test_showPoints_updated(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 1',
        'places': '10'
        }
    purchase_places=client.post('/purchasePlaces', data = credentials)
    response = client.get('/points')
    assert b'Club 1' in response.data
    assert b'<td>10</td>' in response.data
    assert b'Club 2' in response.data
    assert b'<td>15</td>' in response.data