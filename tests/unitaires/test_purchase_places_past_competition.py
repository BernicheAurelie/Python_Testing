from tests.mocks import mocker_clubs, mocker_competitions, mocker_past_competitions
from tests.fixture import client


def test_purchase_places_in_past_competition(mocker, client):
    mocker_clubs(mocker)
    mocker_past_competitions(mocker)
    email = 'club2@test.com'
    response = client.post('/showSummary', data={'email' : email})
    assert response.status_code == 200
    assert b'Summary' in response.data
    assert b'Book Places' not in response.data
    