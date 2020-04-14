import os

from django.urls import path, include
from user import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='user.login'),
    path('logout/', views.logout_page, name='user.logout'),
    path('password-reset/', include([
        path('', views.PasswordResetView.as_view(), name='user.password.reset'),
        path('done/', views.PasswordResetView.as_view(template_name=os.path.join('password', 'reset-done.html')),
             name='user.password.reset.done'),
        path(
            'complete/',
            views.PasswordResetCompleteView.as_view(),
            name='user.password.reset.complete'),
        path(
            '<uidb64>/<token>/',
            views.PasswordResetConfirmView.as_view(),
            name='user.password.reset.confirm'),
    ])),
    path(
        'password-change/',
        views.PasswordChangeView.as_view(),
        name='user.password.change'),
]
