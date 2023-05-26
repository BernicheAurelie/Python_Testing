import server


def mocker_clubs(mocker):
    mocker.patch.object(server,'clubs', [
        {
            "name":"Club 1",
            "email":"club1@test.com",
            "points":"20"
        },
        {
            "name":"Club 2",
            "email": "club2@test.com",
            "points":"15"
            
        },
        {
            "name":"Club 3",
            "email": "club3@test.com",
            "points":"5"
            
        },
        {
            "name":"Club 4",
            "email": "club4@test.com",
            "points":"50"
        }, 
        {
            "name":"Club 5",
            "email": "club5@test.com",
            "points":"21"
        }])

def mocker_competitions(mocker):
    mocker.patch.object(server,'competitions', [
        {
            "name":"Competition 1",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name":"Competition 2",
            "date": "2021-03-27 10:00:00",
            "numberOfPlaces": "25"
            
        },
        {
            "name":"Competition 3",
            "date": "2024-05-16 10:00:00",
            "numberOfPlaces": "10"
            
        }])

def mocker_past_competitions(mocker):
    mocker.patch.object(server,'competitions', [
        {
            "name":"Competition 1",
            "date": "2021-03-27 10:00:00",
            "numberOfPlaces": "25"
            
        },
        {
            "name":"Competition 2",
            "date": "2023-05-16 10:00:00",
            "numberOfPlaces": "10"
            
        }])