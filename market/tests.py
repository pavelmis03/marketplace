from django import test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.test import Client


class URLTests(test.TestCase):
    def setUp(self):
        self.test_username = 'vasya'
        self.test_pass = 'promprog'
        self.client = Client()

    def test_authorization_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_catalogue_page(self):
        response = self.client.get('/catalogue/')
        self.assertEqual(response.status_code, 200)

    def test_basket_page(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)

    def test_offers_page(self):
        response = self.client.get('/offers/')
        self.assertEqual(response.status_code, 200)

    def test_search_page(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

    def test_yamaps_page(self):
        response = self.client.get('/ya_maps/')
        self.assertEqual(response.status_code, 200)

    def test_yasafety_page(self):
        response = self.client.get('/ya_safety/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_reports_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/reports/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_orders_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/orders/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_orders_statistics_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/orders/statistics/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_users_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/users/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_partners_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/partners/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_alerts_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/users/alerts/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_ranges_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/ranges/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_catalogue_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/catalogue/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_catalogue_alerts_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/catalogue/stock-alerts/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_catalogue_options_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/catalogue/option/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_reviews_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/reviews/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_comms_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/comms/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_pages_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/dashboard/pages/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_profile_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/profile/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_orders_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/orders/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_addressbook_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/addresses/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_emails_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/emails/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_alerts_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/alerts/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_notifications_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/notifications/inbox/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_notifications_archive_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/notifications/archive/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_wishlists_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/wishlists/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_wishlists_create_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/wishlists/create/', follow=True)
        self.assertEqual(response.status_code, 200)
