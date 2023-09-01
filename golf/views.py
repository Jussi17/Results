import requests
from django.shortcuts import render

def golfindex(request):
    url = 'https://api.sportsdata.io/golf/v2/json/Leaderboard/541?key=4268c11493fc4ad7b68d1cc05177d96e'
    response = requests.get(url)
    leaderboard_data = response.json()

    players = leaderboard_data.get('Players', [])
    sorted_players = sorted(players, key=lambda player: player.get('Rank', float('inf')) or float('inf'))

    context = {
        'players': sorted_players,
    }

    return render(request, 'golf/index.html', context)

def golfpga(request):
    url = 'https://api.sportsdata.io/golf/v2/json/Leaderboard/547?key=4268c11493fc4ad7b68d1cc05177d96e'
    response = requests.get(url)
    leaderboard_data = response.json()

    players = leaderboard_data.get('Players', [])
    sorted_players = sorted(players, key=lambda player: player.get('Rank', float('inf')) or float('inf'))

    context = {
        'players': sorted_players,
    }

    return render(request, 'golf/pga.html', context)

def golfusopen(request):
    url = 'https://api.sportsdata.io/golf/v2/json/Leaderboard/551?key=4268c11493fc4ad7b68d1cc05177d96e'
    response = requests.get(url)
    leaderboard_data = response.json()

    players = leaderboard_data.get('Players', [])
    sorted_players = sorted(players, key=lambda player: player.get('Rank', float('inf')) or float('inf'))

    context = {
        'players': sorted_players,
    }

    return render(request, 'golf/usopen.html', context)

def golftheopen(request):
    url = 'https://api.sportsdata.io/golf/v2/json/Leaderboard/558?key=4268c11493fc4ad7b68d1cc05177d96e'
    response = requests.get(url)
    leaderboard_data = response.json()

    players = leaderboard_data.get('Players', [])
    sorted_players = sorted(players, key=lambda player: player.get('Rank', float('inf')) or float('inf'))

    context = {
        'players': sorted_players,
    }

    return render(request, 'golf/theopen.html', context)
    
