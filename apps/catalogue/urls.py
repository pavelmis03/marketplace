"""URLs for 'API' app"""
from django.urls import path

from apps.catalogue import views

urlpatterns = [
    # Your other URLs
    # url(r'', include(catalogue.urls)),
    path('market/<slug:slug>/', views.market_detail_view, name='market-detail'),
]
