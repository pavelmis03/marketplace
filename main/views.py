"""Views for 'main' app"""
import requests
from django.shortcuts import render

BAD_SITES = [
    {'url': 'https://ydx-malware-driveby-shavar.cepera.ru'},
    {'url': 'https://ydx-phish-shavar.cepera.ru'},
    {'url': 'https://testsafebrowsing.appspot.com/s/phishing.html'},
    {'url': 'https://testsafebrowsing.appspot.com/s/malware.html'},
    {'url': 'http://malware-driveby.test.safebrowsing.yandex'}
]


def ya_maps_page(request):
    """
    Страница Яндекс-Карт

    :param request: объект c деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    return render(request, 'pages/ya_maps.html', {'pagename': "Карты"})


def ya_safetly_page(request):
    """
    Страница Яндекс-Безопасность

    :param request: объект c деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: перенаправление на главную страницу в случае POST-запроса
    :rtype: :class:`django.http.HttpResponse`
    """
    context = {
        'pagename': "Проверка сайта",
        'site_safety': 0,
        'description': ''
    }

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
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING",
                                "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE",
                                "POTENTIALLY_HARMFUL_APPLICATION"],
                "platformTypes": ["ALL_PLATFORMS"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [{'url': inp}]
            }
        }
        pr = requests.post(
            url='https://sba.yandex.net/v4/threatMatches:find?key=' + key,
            json=data)
        print(pr, pr.text, 1)
        try:
            json = pr.json()
            if json == {}:  # The site is secure
                context['site_safety'] = 1
            else:  # The site is NOT secure
                context['site_safety'] = 2
                context['description'] = str(json['matches'][0]['threatType'])
        except Exception:
            context['site_safety'] = 3
            context['description'] = str(pr)
    return render(request, 'pages/ya_safety.html', context)
