from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="WhatsApp-Automation"),
    path('sendMessage/', views.send_Message, name='sendMessage page'),
    path('sendFile/', views.send_File, name='sendFile page'),
    path('sendMessage/mssg/', views.mssg, name='sendingMsg page'),
    path('sendFile/file/', views.file, name='sendingFile page'),
    path('sendMessage/sendFile/file/', views.file, name='sendingFile page'),
    path('sendFile/sendMessage/', views.send_Message, name='sendMessage page'),
    path('sendMessage/sendFile/', views.send_File, name='sendFile page'),
    
]
