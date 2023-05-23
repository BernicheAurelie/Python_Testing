from tests.mocks import mocker_clubs, mocker_competitions, mocker_past_competitions
from tests.fixture import client


def test_purchase_places_with_points_club_available(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 1',
        'places': '2'
        }
    response = client.post('/purchasePlaces', data = credentials)
    assert response.status_code == 200
    assert b'Points available: 18' in response.data
    assert b'Great-booking complete!' in response.data

def test_purchase_places_without_enough_points_club_available(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 3',
        'places': '6'
        }
    response = client.post('/purchasePlaces', data = credentials)
    print(response.data.decode())
    assert response.status_code == 200
    assert b"Club doesn&#39;t have enough available points" in response.data
    assert b'Points available: 5' in response.data