#django doesnot handle images so we need to handle ourself by importing following two
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('',include('core.urls')),
    # path('contact/',contact,name='contact'),
    # path('items/',include('items.urls')),    # item is the app_name in the url of item app  if the routing of url starts with items/ it will go according to the routing of item app url
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
