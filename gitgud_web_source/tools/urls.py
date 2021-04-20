from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ping/',views.ping, name='ping'),
    path('testping/',views.testping, name='testping'),
    path('testdig/',views.testdig,name='testdig')
]