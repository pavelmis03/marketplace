from django.urls import include, path
from rest_framework import routers
from botapp import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'product-class', views.ProductClassViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'order-note', views.OrderNoteViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'site', views.SiteViewSet)
router.register(r'basket', views.BasketViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls'))
]
