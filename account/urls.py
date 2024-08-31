from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'account'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html', form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register-user/', views.register, name='register_user')
]
