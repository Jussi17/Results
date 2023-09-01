from django.urls import path
from . import views

app_name = 'golf'

urlpatterns = [
    path('', views.golfindex, name='golfindex'),
    path('pga/', views.golfpga, name='golfpga'),
    path('usopen/', views.golfusopen, name='golfusopen'),
    path('theopen/', views.golftheopen, name='golftheopen'),
]