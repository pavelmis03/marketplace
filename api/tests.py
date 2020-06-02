from django.test import TestCase, Client


class APITest(TestCase):
    fixtures = ['simple_db.json']
    USER = {
        'username': 'vasya',
        'email': '1@abc.net',
        'password': 'promprog',
    }
    API_ROOT_URL = '/api/'

    def setUp(self) -> None:
        self.client = Client()
        self.client.login(
            username=self.USER['username'],
            password=self.USER['password'],
        )

    def test_apiRoot(self):
        response = self.client.get(self.API_ROOT_URL)
        self.assertEqual(response.status_code, 200)

    def test_apiAllJson(self):
        response = self.client.get(self.API_ROOT_URL, data={'format': 'json'})
        self.assertEqual(response.status_code, 200)

        for key, url in response.data.items():
            response = self.client.get(url, data={'format': 'json'})
            self.assertEqual(response.status_code, 200)
