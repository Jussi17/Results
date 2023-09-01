from django.urls import path
from . import views

app_name = 'koris'

urlpatterns = [
    path('', views.korisindex, name='korisindex'),
    path('standings/', views.korisstandings, name='korisstandings'),
    path('standingswest/', views.korisstandingswest, name='korisstandingswest'),
    path('boxscore/<int:game_id>/', views.boxscore, name='boxscore'),
]