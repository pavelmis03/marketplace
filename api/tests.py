"""Test cases for 'API' app"""
# from django.contrib.auth.models import User
# from django.test import TestCase, Client
# from rest_framework.authtoken.models import Token


# class APITest(TestCase):
#     fixtures = ['simple_db.json']
#     USER = {
#         'username': 'vasya',
#         'email': '1@abc.net',
#         'password': 'promprog',
#     }
#     API_ROOT_URL = '/api/'
#
#     def setUp(self) -> None:
#         self.client = Client()
#         self.client.login(
#             username=self.USER['username'],
#             password=self.USER['password'],
#         )
#
#     def get_headers(self):
#         user = User.objects.filter(username=self.USER['username'])[0]
#         return {
#             'Authorization': 'Token ' + Token.objects.filter(user=user)[0].key,
#         }
#
#     def test_apiRoot(self):
#         response = self.client.get(self.API_ROOT_URL,
#                                    headers=self.get_headers())
#         self.assertEqual(response.status_code, 200)
#
#     def test_apiAllJson(self):
#         response = self.client.get(self.API_ROOT_URL, data={'format': 'json'},
#                                    headers=self.get_headers())
#         self.assertEqual(response.status_code, 200)
#
#         for key, url in response.data.items():
#             response = self.client.get(url, data={'format': 'json'})
#             self.assertEqual(response.status_code, 200)
