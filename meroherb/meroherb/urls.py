#django doesnot handle images so we need to handle ourself by importing following two
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from item.views import mainpage

app_name="meroherb"

urlpatterns = [

    path('',include('core.urls')),
    path('',include('dashboard.urls')),
    path('',include('item.urls')),
    path('',include('sellerform.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
