from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pingpage/',views.pingpage, name='pingpage'),
    path('digpage/',views.digpage,name='digpage')
]