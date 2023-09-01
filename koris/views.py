from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import datetime
from django import forms

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

def korisindex(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            current_date = form.cleaned_data['date'].strftime('%Y-%b-%d')
        else:
            current_date = datetime.date.today().strftime('%Y-%b-%d')
    else:
        current_date = datetime.date.today().strftime('%Y-%b-%d')
        
    
    games_url = f"https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{current_date}?key=af466c3c380a464b9ee315f621533238"
    logos_url = "https://api.sportsdata.io/v3/nba/scores/json/teams?key=af466c3c380a464b9ee315f621533238"
    
    games_response = requests.get(games_url)
    games_data = games_response.json()
    
    logos_response = requests.get(logos_url)
    logos_data = logos_response.json()
    
    form = DateForm(initial={'date': current_date})
    
    context = {
        'games': games_data,
        'logos': logos_data,
        'form': form,
        'current_date': current_date,

    }
    
    return render(request, 'koris/index.html', context)

def boxscore(request, game_id):
    boxscore_url = f"https://api.sportsdata.io/v3/nba/stats/json/BoxScore/{game_id}?key=af466c3c380a464b9ee315f621533238"
    boxscore_response = requests.get(boxscore_url)
    boxscore_data = boxscore_response.json()
    
    context = {
        'boxscore': boxscore_data,
    }
    
    return render(request, 'koris/boxscore.html', context)

def korisstandings(request):
    standings_url = "https://api.sportsdata.io/v3/nba/scores/json/Standings/2023?key=af466c3c380a464b9ee315f621533238"
    logos_url = "https://api.sportsdata.io/v3/nba/scores/json/teams?key=af466c3c380a464b9ee315f621533238"
    
    standings_response = requests.get(standings_url)
    logos_response = requests.get(logos_url)
    
    standings_data = standings_response.json()
    logos_data = logos_response.json()
    
    combined_data = {
        'standings': standings_data,
        'logos': logos_data
    }
    
    return render(request, 'koris/standings.html', {'jsonResponse': combined_data})

def korisstandingswest(request):
    standings_url = "https://api.sportsdata.io/v3/nba/scores/json/Standings/2023?key=af466c3c380a464b9ee315f621533238"
    logos_url = "https://api.sportsdata.io/v3/nba/scores/json/teams?key=af466c3c380a464b9ee315f621533238"
    
    standings_response = requests.get(standings_url)
    logos_response = requests.get(logos_url)
    
    standings_data = standings_response.json()
    logos_data = logos_response.json()
    
    combined_data = {
        'standings': standings_data,
        'logos': logos_data
    }
    
    return render(request, 'koris/standingswest.html', {'jsonResponse': combined_data})