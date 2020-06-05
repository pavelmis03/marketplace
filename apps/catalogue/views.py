"""Views for 'catalogue' app"""
from django.shortcuts import render
from oscar.apps.catalogue.views import CatalogueView as OscarCatalogueView

from apps.catalogue.models import Market


def market_detail_view(request, slug):
    """
    Страница поиска заданного товара по магазинам

    :param request: объект c деталями запроса
    :param slug: ключевое слово - параметр фильтра
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    context = {
        'found': False,
    }
    markets = Market.objects.filter(slug=slug)

    if markets:
        context['found'] = True
        context['market'] = markets[0]

    return render(request, 'market.html', context)


class CatalogueView(OscarCatalogueView):
    """
    Переопределение CatalogueView, чтобы добавить список магазинов в контекст.
    """
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['markets'] = Market.objects.all()
        return ctx
