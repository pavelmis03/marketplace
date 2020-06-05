"""URLs for 'API' app"""
from django.urls import path

from apps.catalogue import views

urlpatterns = [
    path('market/<slug:slug>/', views.market_detail_view, name='market-detail'),
]
