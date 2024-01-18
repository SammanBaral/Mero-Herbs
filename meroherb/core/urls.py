from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from django.contrib.auth.views import LoginView

app_name='core'

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),name="login"),

]