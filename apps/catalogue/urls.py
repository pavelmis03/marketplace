from django.conf.urls import include, url
from django.urls import path
from oscar.apps import catalogue
from apps.catalogue import views


urlpatterns = [
    # Your other URLs
    # url(r'', include(catalogue.urls)),

    path('market/<slug:slug>', views.market_detail_view),
]
