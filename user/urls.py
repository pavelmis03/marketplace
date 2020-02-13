from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='user.login'),
    path('logout/', views.logout_page, name='user.logout'),
]