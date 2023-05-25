from tests.mocks import mocker_clubs, mocker_competitions, mocker_past_competitions
from tests.fixture import client


def test_purchase_places_and_points_available_updated(mocker, client):
    mocker_clubs(mocker)
    mocker_competitions(mocker)
    credentials = {
        'competition': 'Competition 1',
        'club': 'Club 5',
        'places': '4'
        }
    response1 = client.post('/purchasePlaces', data = credentials)
    print (response1.data.decode())
    assert response1.status_code == 200
    assert b'Points available: 9' in response1.data
    assert b'Great-booking complete!' in response1.data
    credentials_2 = {
        'competition': 'Competition 1',
        'club': 'Club 5',
        'places': '3'
        }
    response2 = client.post('/purchasePlaces', data = credentials_2)
    print (response2.data.decode())
    assert response2.status_code == 200
    assert b"You've no more points available!" in response2.data
    assert b'Great-booking complete!' in response2.data
