from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'item'
urlpatterns =[
    path('new/', views.new, name='new'),
    path('',views.mainpage,name="home"),
    path('main/',views.mainpage,name="main"),
    path('browse/',views.browse,name='browse'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('category/<str:pro>',views.Category_view,name="category_view"),
    path('seller/',views.sellerform,name='sellerform'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
