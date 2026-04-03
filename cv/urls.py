from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cv, name='cv'),
    path('i18n/', include('django.conf.urls.i18n')),
]