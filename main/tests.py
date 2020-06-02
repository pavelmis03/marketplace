# pylint: disable=missing-function-docstring
from django import test
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
        response = self.client.get('/ya/maps/')
        self.assertEqual(response.status_code, 200)

    def test_yasafety_page(self):
        response = self.client.get('/ya/safety/')
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
        response = self.client.get('/dashboard/catalogue/stock-alerts/',
                                   follow=True)
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
        response = self.client.get('/accounts/notifications/inbox/',
                                   follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_notifications_archive_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/notifications/archive/',
                                   follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_wishlists_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/wishlists/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_account_wishlists_create_page(self):
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.get('/accounts/wishlists/create/', follow=True)
        self.assertEqual(response.status_code, 200)

# TODO: Посмотрите и разоберите эти тесты. Тут может быть что-то полезное:
# from django.contrib.auth.models import User
# from django.test import TestCase, Client
# from django.urls import reverse
#
#
# class AuthTest(TestCase):
#     fixtures = ['test_auth_db.json']
#     user = {"username": "vasya", "password": "promprog"}
#     login_url = reverse('login')
#
#     def get_user_object(self):
#         return User.objects.get(username=self.user["username"])
#
#     def setUp(self) -> None:
#         self.client = Client()
#
#     def test_getUser(self):
#         user = self.get_user_object()
#         self.assertTrue(user)
#
#     def test_softAuth(self):
#         self.assertTrue(self.client.login(**self.user))
#         self.client.logout()
#
#     def test_forceAuth(self):
#         self.client.force_login(self.get_user_object())
#         self.client.logout()
#
#     def test_customAuth0(self):
#         response = self.client.get(self.login_url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_customAuth1(self):
#         response = self.client.post(self.login_url, self.user, follow=True)
#         self.assertEqual(response.status_code, 200)
#
#
# class PagesTest(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#
#     def check_response_status(self, url, code=200):
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, code)
#
#     def test_pages(self):
#         self.check_response_status(reverse('index'))
#         self.check_response_status(reverse('riddle'))
#         self.check_response_status(reverse('answer'))
#         self.check_response_status(reverse('multiply'))
#         # self.check_response_status(reverse('expression'))
#         self.check_response_status(reverse('expression_history'))
#         self.check_response_status(reverse('str2words'), 302)
#         self.check_response_status(reverse('str_history'), 302)
#         self.check_response_status(reverse('calc'), 302)
#
#
# class MainTest(TestCase):
#     fixtures = ['test_db.json']
#
#     def setUp(self) -> None:
#         username = "vasya"
#         self.client = Client()
#         self.client.force_login(User.objects.get(username=username))
#
#     def test_multiply0(self):
#         response = self.client.get(reverse('multiply'))
#         self.assertFalse(response.context['got_value'])
#
#     def test_multiply1(self):
#         url = reverse('multiply')
#         for value in range(100):
#             response = self.client.get(url, {'value': value})
#             self.assertEqual(response.context['value'], value)
#             self.assertEqual(response.context['items'],
#             [dict(a=i, b=value, c=i * value) for i in range(1, 11)])
#
#     def test_expression(self):
#         response = self.client.get(reverse('expression'))
#         expression = response.context['expression']
#         items = []
#         for i in range(1, 5):
#             value = getattr(expression, "a{}".format(i))
#             if value is not None:
#                 items.append(value)
#         self.assertEqual(sum(items), expression.result)
#
#     def test_str2words0(self):
#         response = self.client.get(reverse('str2words'))
#         self.assertIn('form', response.context)
#         self.assertIsNotNone(response.context['form'])
#         self.assertFalse(response.context['form'].is_valid())
#
#     def test_calc0(self):
#         a, b = 3, 4
#         response = self.client.post(reverse('calc'),
#         {'first': a, 'second': b})
#         self.assertEqual(response.context['form_result'].initial['answer'],
#         a + b)
#
#     def test_calc1(self):
#         a, b = 274, 262
#         response = self.client.post(reverse('calc'),
#         {'first': a, 'second': b})
#         self.assertEqual(response.context['form_result'].initial['answer'],
#         a + b)
#
#     def test_calc2(self):
#         a, b = 723, 253
#         response = self.client.post(reverse('calc'), {'first': a,
#         'second': b})
#         self.assertEqual(response.context['form_result'].initial['answer'],
#         a + b)
#
#     def test_calc3(self):
#         a, b = 135, 135
#         response = self.client.post(reverse('calc'),
#         {'first': a, 'second': b})
#         self.assertEqual(response.context['form_result'].initial['answer'],
#         a + b)
#
#     def test_calc4(self):
#         a, b = 364, 753
#         response = self.client.post(reverse('calc'),
#         {'first': a, 'second': b})
#         self.assertEqual(response.context['form_result'].initial['answer'],
#         a + b)
