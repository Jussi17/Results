from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import datetime
from django import forms

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

def hokiindex(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            current_date = form.cleaned_data['date'].strftime('%Y-%b-%d')
        else:
            current_date = datetime.date.today().strftime('%Y-%b-%d')
    else:
        current_date = datetime.date.today().strftime('%Y-%b-%d')
    
    games_url = f"https://api.sportsdata.io/v3/nhl/scores/json/GamesByDate/{current_date}?key=d9e8a70486a8437596e6d54551f282c9"
    logos_url = "https://api.sportsdata.io/v3/nhl/scores/json/AllTeams?key=d9e8a70486a8437596e6d54551f282c9"
    
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
    
    return render(request, 'hoki/index.html', context)


def boxscore(request, game_id):
    boxscore_url = f"https://api.sportsdata.io/v3/nhl/stats/json/BoxScore/{game_id}?key=d9e8a70486a8437596e6d54551f282c9"
    boxscore_response = requests.get(boxscore_url)
    boxscore_data = boxscore_response.json()
    
    player_url = "https://api.sportsdata.io/v3/nhl/scores/json/Players?key=d9e8a70486a8437596e6d54551f282c9"
    player_response = requests.get(player_url)
    player_data = player_response.json()
    
    context = {
        'boxscore': boxscore_data,
        'player': player_data,
    }
    
    return render(request, 'hoki/boxscore.html', context)

def hokistandings(request):
    standings_url = "https://api.sportsdata.io/v3/nhl/scores/json/Standings/2023?key=d9e8a70486a8437596e6d54551f282c9"
    logos_url = "https://api.sportsdata.io/v3/nhl/scores/json/AllTeams?key=d9e8a70486a8437596e6d54551f282c9"
    
    standings_response = requests.get(standings_url)
    logos_response = requests.get(logos_url)
    
    standings_data = standings_response.json()
    logos_data = logos_response.json()
    
    combined_data = {
        'standings': standings_data,
        'logos': logos_data
    }
    
    return render(request, 'hoki/standings.html', {'jsonResponse': combined_data})

def hokistandingswest(request):
    standings_url = "https://api.sportsdata.io/v3/nhl/scores/json/Standings/2023?key=d9e8a70486a8437596e6d54551f282c9"
    logos_url = "https://api.sportsdata.io/v3/nhl/scores/json/AllTeams?key=d9e8a70486a8437596e6d54551f282c9"
    
    standings_response = requests.get(standings_url)
    logos_response = requests.get(logos_url)
    
    standings_data = standings_response.json()
    logos_data = logos_response.json()
    
    combined_data = {
        'standings': standings_data,
        'logos': logos_data
    }
    
    return render(request, 'hoki/standingswest.html', {'jsonResponse': combined_data})