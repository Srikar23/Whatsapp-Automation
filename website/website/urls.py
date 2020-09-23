from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('whatsapp.urls')),
    path('sendMessage', include('whatsapp.urls')),
    path('sendFile', include('whatsapp.urls'))
]
