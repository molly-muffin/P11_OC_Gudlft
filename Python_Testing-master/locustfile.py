from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        response = self.client.get("/")

    @task
    def boardpoints(self):
        response = self.client.get("/boardpoints")

    @task
    def login(self):
        response = self.client.post(
            "/showSummary", {"email": "john@simplylift.co"})

    @task
    def book_link(self):
        response = self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def purchase_place(self):
        response = self.client.post(
            '/purchasePlaces', data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": 3})

    @task
    def logout(self):
        response = self.client.get('/logout')
