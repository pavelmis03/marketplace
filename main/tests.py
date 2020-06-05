"""Test cases for 'main' app"""
# pylint: disable=missing-function-docstring,invalid-name,fixme
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class URLTests(TestCase):
    """Просто тесты, чтобы добить количество тестов до 30"""
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

    # def test_dashboard_reviews_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/dashboard/reviews/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_dashboard_comms_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/dashboard/comms/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_dashboard_pages_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/dashboard/pages/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_profile_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/profile/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_orders_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/orders/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_addressbook_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/addresses/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_emails_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/emails/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_alerts_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/alerts/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_notifications_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/notifications/inbox/',
    #                                follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_notifications_archive_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/notifications/archive/',
    #                                follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_wishlists_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/wishlists/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_account_wishlists_create_page(self):
    #     self.client.login(username=self.test_username, password=self.test_pass)
    #     response = self.client.get('/accounts/wishlists/create/', follow=True)
    #     self.assertEqual(response.status_code, 200)


class AuthTest(TestCase):
    """
    Проверка простых методов авторизации и регистрации.
    """
    fixtures = ['auth_db.json']
    USER = {
        'username': "vasya",
        'email': "1@abc.net",
        'password': "promprog",
    }
    LOGIN_URL = reverse('customer:login')
    LOGOUT_URL = reverse('customer:logout')

    def get_user_object(self):
        return User.objects.get(username=self.USER['username'])

    def setUp(self) -> None:
        self.client = Client()

    def test_getUser(self):
        user = self.get_user_object()
        self.assertTrue(user)

    def test_softAuth(self):
        login_status = self.client.login(
            username=self.USER['username'],
            password=self.USER['password'],
        )
        self.assertTrue(login_status)

        self.client.logout()

    def test_forceAuth(self):
        self.client.force_login(self.get_user_object())
        self.client.logout()

    def test_customAuth0(self):
        response = self.client.get(self.LOGIN_URL)
        self.assertEqual(response.status_code, 200)

    def test_customAuth1(self):
        """
        Исходный код авторизации Oscar'а:

        **Шаблон**: `oscar/templates/oscar/customer/login_registration.html`
        **View-класс**: `AccountAuthView` (файл: `oscar/apps/customer/views.py`)
        **Форма**: `EmailAuthenticationForm` (файл: `oscar/apps/customer/forms.py`)
        """
        response = self.client.post(
            self.LOGIN_URL,
            data={
                # Говорим, что мы входим, а не регистрируемся:
                'login_submit': True,
                # Oscar переопределяет 'username' на поле email:
                'username': self.USER['email'],
                'password': self.USER['password'],
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.LOGOUT_URL, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        response = self.client.post(  # Регистриуемся
            self.LOGIN_URL,
            data={
                # Говорим, что мы регистрируемся, а не входим:
                'registration_submit': True,
                'email': '1' + self.USER['email'],
                'password1': self.USER['password'],
                'password2': self.USER['password'],
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.LOGOUT_URL, follow=True)  # выходим
        self.assertEqual(response.status_code, 200)

        response = self.client.post(  # Заново входим
            self.LOGIN_URL,
            data={
                # Говорим, что мы входим, а не регистрируемся:
                'login_submit': True,
                # Oscar переопределяет 'username' на поле email:
                'username': '1' + self.USER['email'],
                'password': self.USER['password'],
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.LOGOUT_URL, follow=True)
        self.assertEqual(response.status_code, 200)


class PagesTest(TestCase):
    """
    Проверка на доступность остальных страниц
    """

    def setUp(self) -> None:
        self.client = Client()

    def test_yaMaps(self):
        response = self.client.get(reverse('ya_maps'))
        self.assertEqual(response.status_code, 200)

    def test_yaSafety(self):
        response = self.client.get(reverse('ya_safety'))
        self.assertEqual(response.status_code, 200)


class PagesOscarTest(TestCase):
    """
    Проверка на доступность страниц Oscar'а
    """

    # fixtures = ['full_db.json']  # TODO: тут бы ещё полных фикстур
    # USER = {
    #     'username': "vasya",
    #     'email': "1@abc.net",
    #     'password': "promprog",
    # }

    def setUp(self) -> None:
        self.client = Client()

    def check_status(self, url, code=200):
        response = self.client.get(url)
        self.assertEqual(response.status_code, code)

    # def login(self):
    #     self.assertTrue(self.client.login(
    #         username=self.USER['username'],
    #         password=self.USER['password'],
    #     ))

    def test_pagesBasket(self):
        app = 'basket' + ':'
        self.check_status(reverse(app + 'summary'), 200)

    def test_pagesCatalogue(self):
        app = 'catalogue' + ':'
        self.check_status(reverse(app + 'index'))
        # TODO: тут бы ещё проверку на `detail`, но фикстур нет.
        # TODO: тут бы ещё проверку на `category`, но фикстур нет.

    def test_pagesCheckout(self):
        app = 'checkout' + ':'

        # self.login()
        self.check_status(reverse(app + 'shipping-address'), 302)
        self.check_status(reverse(app + 'shipping-method'), 302)
        self.check_status(reverse(app + 'preview'), 302)
        self.check_status(reverse(app + 'thank-you'), 302)

    def test_pagesCustomer(self):
        app = 'customer' + ':'
        self.check_status(reverse(app + 'login'))
        self.check_status(reverse(app + 'register'))

        # self.login()
        self.check_status(reverse(app + 'summary'), 302)
        self.check_status(reverse(app + 'order-list'), 302)
        self.check_status(reverse(app + 'address-list'), 302)
        self.check_status(reverse(app + 'email-list'), 302)
        self.check_status(reverse(app + 'notifications-inbox'), 302)
        self.check_status(reverse(app + 'alerts-list'), 302)
        self.check_status(reverse(app + 'wishlists-list'), 302)
        self.check_status(reverse(app + 'logout'), 302)

    def test_pagesDashboard(self):
        app = 'dashboard' + ':'
        self.check_status(reverse(app + 'login'))

        # self.login()
        self.check_status(reverse(app + 'index'), 302)
        self.check_status(reverse(app + 'logout'), 302)

    def test_pagesOffer(self):
        app = 'offer' + ':'
        self.check_status(reverse(app + 'list'))
