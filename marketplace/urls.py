"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main import views as main_views
from marketplace import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Oscar
    path('oscar/', include(apps.get_app_config('oscar').urls[0]), name='oscar'),


    # Подмагазины
    path('', include('apps.catalogue.urls')),

    # API & bot
    path('api/', include('botapp.urls')),

    # Яндек-интеграции
    path('ya_safety/', main_views.time_page, name='ya_safety'),
    path('ya_maps/', main_views.ya_maps, name='ya_maps'),

    # Остальное
    path('', main_views.index_page, name='index'),
    path('user/', include('user.urls')),
    # path('time/', main_views.time_page, name='time'),
    # path('market/', include('market.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
