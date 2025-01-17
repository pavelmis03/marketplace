"""Тут контекстные процессоры, которые добавляют в контекст необходимые вещи"""
from django.http import HttpRequest

from apps.catalogue.models import Market


def navbar(request: HttpRequest):
    """
    Стандартные контекстный процессор для получения пунктов меню.

    :param request: объект c деталями запроса. Используется для получения
    авторизованного пользователя
    :type request: :class:`django.http.HttpRequest`
    :return: словарь с предустановленными значениями
    :rtype: :class:`dict`
    """
    is_auth = False
    is_staff = False

    if hasattr(request, 'user'):
        is_auth = request.user.is_authenticated
        is_staff = request.user.is_staff

    extra_context = {
        'navbar': [],
        'user_navbar': [],
    }

    if not is_auth:  # TODO: переопределите, если нужно  # pylint: disable=fixme
        extra_context['user_navbar'] = [
            {'url_name': 'login', 'name': 'Вход'},
            {'url_name': 'index', 'name': 'Регистрация'},
        ]
    else:
        extra_context['user_navbar'] = [
            {'url_name': 'index', 'name': 'Профиль'},
            {'url_name': 'logout', 'name': 'Выйти'},
        ]
        if is_staff:
            extra_context['navbar'] = [
                {'url_name': 'event.list', 'name': 'События'},
                {'url_name': 'index', 'name': 'Игроки'},
            ]
    return extra_context


def market_list(request: HttpRequest):
    """Добавляет список всех подмагазинов"""
    extra_context = {
        'markets': Market.objects.all(),
    }
    return extra_context
