from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

app_name='core'

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),name="login"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"), 
    path('main/',views.mainpage,name="main"),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)