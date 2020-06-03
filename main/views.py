import requests
from django.shortcuts import render
from django.utils import timezone

bad_sites = [
    {'url': 'https://ydx-malware-driveby-shavar.cepera.ru'},
    {'url': 'https://ydx-phish-shavar.cepera.ru'},
    {'url': 'https://testsafebrowsing.appspot.com/s/phishing.html'},
    {'url': 'https://testsafebrowsing.appspot.com/s/malware.html'},
    {'url': 'http://malware-driveby.test.safebrowsing.yandex'}
]


def get_base_context(request, pagename='UNTITLED'):
    """
    Получение базового контекста

    :param request: объект c деталями запроса. Используется для получения авторизованного пользователя
    :type request: :class:`django.http.HttpRequest`
    :param pagename: название страницы, по умолчанию его значение 'UNTITLED'
    :return: словарь с предустановленными значениями
    """
    context = {
        'pagename': pagename,
        'navbar': [
            {'url_name': 'index', 'name': 'Главная'},
        ],
        'right_navbar': [],
    }

    if not request.user.is_authenticated:
        context['right_navbar'] += [
            {'url_name': 'user.login', 'name': 'Войти'},
        ]
    else:
        context['navbar'] += [
            {'url_name': 'index', 'name': 'Для авторизированных'},
            {'url_name': 'index', 'name': 'Ещё что-то'},
        ]
        context['right_navbar'] += [
            {'url_name': 'index', 'name': 'Профиль: {}'.format(request.user)},
            {'url_name': 'user.logout', 'name': 'Выйти'},
        ]

    return context


def index_page(request):
    """
    Главная страница

    :param request: объект c деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    context = get_base_context(request, "Главная")
    return render(request, 'pages/index.html', context)


def ya_maps(request):
    """
    Страница Яндекс-Карты

    :param request: объект c деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    context = get_base_context(request, "Карты")
    return render(request, 'pages/ya_maps.html', context)

def time_page(request):
    """
    Страница 'Дата и время'

    :param request: объект c деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: перенаправление на главную страницу в случае POST-запроса
    """
    context = get_base_context(request, "Проверка сайта")
    context['time'] = timezone.now().time()
    context['site_safety'] = 0
    context['description'] = ''
    if request.POST:
        inp = request.POST.get("f_textBox", "")
        print("Input data: " + inp)
        key = 'a93a671e-2e42-4041-a3b1-882ba247844b'
        data = {
            "client": {
                "clientId": "3214123",
                "clientVersion": "3123"
            },
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE",
                                "POTENTIALLY_HARMFUL_APPLICATION"],
                "platformTypes": ["ALL_PLATFORMS"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [ {'url': inp} ]
            }
        }
        pr = requests.post(url='https://sba.yandex.net/v4/threatMatches:find?key=' + key, json=data)
        print(pr, pr.text, 1)
        try:
            json = pr.json()
            if json == {}:  # The site is secure
                context['site_safety'] = 1
            else:  # The site is NOT secure
                context['site_safety'] = 2
                context['description'] = str(json['matches'][0]['threatType'])
        except:
            context['site_safety'] = 3
            context['description'] = str(pr)
    return render(request, 'pages/ya_safety.html', context)

def view_docs(request):
    return render(request, 'build/html/index.html', {})
