from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


router = routers.DefaultRouter()
# router.register(r'users', views.user_list)
router.register(r'groups', views.GroupViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'product-class', views.ProductClassViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'order-line', views.OrderLineViewSet)
router.register(r'order-note', views.OrderNoteViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'site', views.SiteViewSet)
router.register(r'basket', views.BasketViewSet)
router.register(r'basket-line', views.BasketLineViewSet)
router.register(r'shippingaddress', views.ShippingAddressViewSet)
router.register(r'stockrecord', views.StockRecordViewSet)
router.register(r'partner', views.PartnerViewSet)


urlpatterns = [
    # path('user-list', views.user_list, name="user-list"),
    # path('user-detail/<int:pk>', views.user_detail, name="user-detail"),
    path('user-list', views.UserList.as_view(), name="user-list"),
    path('user-detail/<int:pk>', views.UserDetail.as_view(), name="user-detail"),
    # path('product-list', views.ProductList.as_view(), name="product-list"),
    # path('product-detail/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('', include('rest_framework.urls')),
    path('', include(router.urls)),
]
