from django.shortcuts import render
from oscar.apps.catalogue.views import CatalogueView as OscarCatalogueView

from apps.catalogue.models import Market


def market_detail_view(request, slug):
    context = {
        'found': False,
    }
    markets = Market.objects.filter(slug=slug)

    if markets:
        context['found'] = True
        context['market'] = markets[0]

    return render(request, 'market.html', context)


# Переопределение CatalogueView, чтобы добавить список магазинов в контекст.
class CatalogueView(OscarCatalogueView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['markets'] = Market.objects.all()
        return ctx
