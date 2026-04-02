from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('cv/', views.cv, name='cv'), 
    path('i18n/', include('django.conf.urls.i18n')),
]