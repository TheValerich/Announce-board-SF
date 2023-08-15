from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import UserRegisterForm
from django.contrib.auth.models import User


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class UserLogoutView(LogoutView):
    next_page = 'login_url'


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = '/posts/'
