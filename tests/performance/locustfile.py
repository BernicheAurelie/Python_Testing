from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def index(self):
        response = self.client.get("/")

    @task
    def points(self):
        response = self.client.get("/points")

    @task
    def showSummary(self):
        email = 'john@simplylift.co'
        response = self.client.post('/showSummary', data={'email' : email})

    @task
    def showSummaryBadEmail(self):
        email = 'test@test.com'
        response = self.client.post('/showSummary', data={'email' : email})

    @task
    def logout(self):
        # response = self.client.get("/logout", follow_redirects=True)
        response = self.client.get("/logout")


    @task
    def purchasePlaces(self):
        email = 'john@simplylift.co'
        response = self.client.post('/showSummary', data={'email' : email})
        credentials = {
            'competition': 'Spring Festival',
            'club': 'Simply Lift',
            'places': '2'
            }
        response_2 = self.client.post('/purchasePlaces', data = credentials)

    @task
    def purchasePlacesWithoutPlacesRequired(self):
        email = 'john@simplylift.co'
        response = self.client.post('/showSummary', data={'email' : email})
        credentials = {
            'competition': 'Spring Festival',
            'club': 'Simply Lift',
            'places': ''
            }
        response_2 = self.client.post('/purchasePlaces', data = credentials)

    @task
    def book(self):
        response = self.client.get('/book/Spring%20Festival/Simply%20Lift')

