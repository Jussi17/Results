from django.urls import path, re_path
from . import views

app_name = 'f1'

urlpatterns = [
    path('races/', views.races, name='races'),
    path('', views.f1standings, name='f1standings'),
]