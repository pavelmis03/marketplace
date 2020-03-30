from django.conf.urls import include, url
from oscar.apps import catalogue
from apps.catalogue import views


urlpatterns = [
    # Your other URLs
    # url(r'', include(catalogue.urls)),

    url(r'market/<slug:slug>', views.market_view),
]

