from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('chat/', views.chat, name='chat'),
    # Add more URL patterns as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)