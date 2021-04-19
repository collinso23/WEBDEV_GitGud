from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('network_tools/',views.network_tools, name='network_tools'),
    path('testping/',views.testping, name='testping'),
    path('testdig/',views.testdig,name='testdig')
]