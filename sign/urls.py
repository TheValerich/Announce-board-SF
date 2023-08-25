from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView, user_activate


urlpatterns = [
    path('', UserLoginView.as_view(), name='login_url'),
    path('logout/', UserLogoutView.as_view(), name='logout_url'),
    path('signup/', UserRegisterView.as_view(template_name='registration/signup.html'), name='signup_url'),
    path('register/activate/', user_activate, name='register_activate_url'),

]
