from django.urls import path, include
from . import views
from core import urls

app_name='dashboard'

urlpatterns=[
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('',include('item.urls')),

]