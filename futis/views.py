from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import datetime
from django import forms

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

def index(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            current_date = form.cleaned_data['date'].strftime('%Y-%m-%d')
        else:
            current_date = datetime.date.today().strftime('%Y-%m-%d')
    else:
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        
    
    games_url = f"https://apiv3.apifootball.com/?action=get_events&league_id=149&from={current_date}&to={current_date}&APIkey=c6f3024c4c6a922df6e4f175e1c70d8b239723e5b3777de5812a952ea92301b8"
    
    games_response = requests.get(games_url)
    games_data = games_response.json()
    
    form = DateForm(initial={'date': current_date})
    
    context = {
        'games': games_data,
        'form': form,
        'current_date': current_date,

    }
    
    return render(request, 'futis/index.html', context)

def boxscore(request, match_id):
    boxscore_url = f"https://apiv3.apifootball.com/?action=get_events&league_id=149&match_id={match_id}&APIkey=c6f3024c4c6a922df6e4f175e1c70d8b239723e5b3777de5812a952ea92301b8"
    boxscore_response = requests.get(boxscore_url)
    try:
        boxscore_data = boxscore_response.json()[0]
    except IndexError:
        boxscore_data = None
  
    context = {
        'boxscores': [boxscore_data],
    }
    
    return render(request, 'futis/boxscore.html', context)



def isthmian(request):
    url = "https://apiv3.apifootball.com/?action=get_standings&league_id=149&APIkey=c6f3024c4c6a922df6e4f175e1c70d8b239723e5b3777de5812a952ea92301b8"
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request,'futis/standings.html', {'jsonResponse': jsonResponse})

def central(request):
    url = "https://apiv3.apifootball.com/?action=get_standings&league_id=149&APIkey=c6f3024c4c6a922df6e4f175e1c70d8b239723e5b3777de5812a952ea92301b8"
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request,'futis/standingscentral.html', {'jsonResponse': jsonResponse})

def north(request):
    url = "https://apiv3.apifootball.com/?action=get_standings&league_id=149&APIkey=c6f3024c4c6a922df6e4f175e1c70d8b239723e5b3777de5812a952ea92301b8"
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request,'futis/standingsnorth.html', {'jsonResponse': jsonResponse})

def south(request):
    url = "https://apiv3.apifootball.com/?action=get_standings&league_id=149&APIkey=c6f3024c4c6a922df6e4f175e1c70d8b239723e5b3777de5812a952ea92301b8"
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request,'futis/standingssouth.html', {'jsonResponse': jsonResponse})
