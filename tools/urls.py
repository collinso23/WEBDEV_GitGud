from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testping/',views.ping, name='ping'),
    path('testdig/',views.dig,name='dig'),
    path('testmtr/',views.mtr,name='mtr')
]