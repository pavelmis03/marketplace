from django.shortcuts import render
from django.utils import timezone


def get_base_context(request, pagename='UNTITLED'):
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
    context = get_base_context(request, "Главная")
    return render(request, 'pages/index.html', context)


def time_page(request):
    context = get_base_context(request, "Главная")
    context['time'] = timezone.now().time()
    return render(request, 'pages/time.html', context)
