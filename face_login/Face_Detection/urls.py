from django.conf.urls.static import static
from django.conf.urls.static import settings
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name = "home"),
    path('register/',register,name = 'register'),
    path('login/',login,name = 'login'),
    path('greeting/<face_id>/',Greeting,name='greeting'),
    # path('image/', image_view, name='image_view'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
