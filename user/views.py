import os

from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import reverse_lazy

from main.views import get_base_context


class DetailViewContextDefined():
    pagename = 'unnamed'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_base_context(self.request, self.pagename))
        return context


class LoginView(auth_views.LoginView, DetailViewContextDefined):
    pagename = 'Авторизация'
    template_name = os.path.join('login.html')
    success_url = 'index'


def logout_page(request):
    auth.logout(request)
    return redirect('index')


class PasswordResetView(auth_views.PasswordResetView, DetailViewContextDefined):
    pagename = 'Сброс пароля'
    template_name = os.path.join('password', 'reset-form.html')
    email_template_name = os.path.join('password', 'reset-email.html')
    success_url = reverse_lazy('user.password.reset.done')


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView, DetailViewContextDefined):
    pagename = 'Сброс пароля'
    template_name = os.path.join('password', 'reset-complete.html')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView, DetailViewContextDefined):
    pagename = 'Сброс пароля'
    template_name = os.path.join('password', 'reset-confirm.html')
    success_url = reverse_lazy('user.password.reset.complete')


class PasswordChangeView(auth_views.PasswordChangeView, DetailViewContextDefined):
    pagename = 'Изменение пароля'
    template_name = os.path.join('password', 'change-form.html')
    success_url = 'index'
