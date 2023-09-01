from django.urls import path
from . import views

app_name = 'hoki'

urlpatterns = [
    path('', views.hokiindex, name='hokiindex'),
    path('standings/', views.hokistandings, name='hokistandings'),
    path('standingswest/', views.hokistandingswest, name='hokistandingswest'),
    path('boxscore/<int:game_id>/', views.boxscore, name='boxscore'),
]