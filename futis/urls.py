from django.urls import path
from . import views

app_name = 'futis'

urlpatterns = [
    path('', views.index, name='index'),
    path('isthmian/', views.isthmian, name='isthmian'),
    path('northern/', views.north, name='north'),
    path('central/', views.central, name='central'),
    path('south/', views.south, name='south'),
    path('boxscore/<int:match_id>/', views.boxscore, name='boxscore'),
]

#https://apiv3.apifootball.com/?action=get_events&league_id=149&from=2023-01-01&to=2023-06-06&APIkey=c6f3024c4c6a922df6e4f175e1c70d8b239723e5b3777de5812a952ea92301b8
