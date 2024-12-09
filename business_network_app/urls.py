from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('register/', register, name='register'),
    path('register/', company_register, name='register'),
    path('login/', company_login, name='login'),
    path('test', testmethod, name='testmethod'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)