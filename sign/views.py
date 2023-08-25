from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from .models import UserRegisterForm
from django.contrib.auth.models import User
from board.models import Author


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class UserLogoutView(LogoutView):
    next_page = 'login_url'


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = '/posts/'


def user_activate(request):
    user = get_object_or_404(Author)
    if user.is_activated:
        template = 'registration/user_is_activated.html'
    else:
        template = 'registration/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)
