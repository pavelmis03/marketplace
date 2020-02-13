from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

from main.views import get_base_context


class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    pagename = 'Авторизация'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_base_context(self.request, self.pagename))
        return context


def logout_page(request):
    auth.logout(request)
    return redirect('index')
