from django.urls import path

from market.views import product_list, product_detail

app_name = 'market'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<str:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<str:slug>/', product_detail, name='product_detail')
]
