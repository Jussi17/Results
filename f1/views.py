from django.shortcuts import render
import requests
from json.decoder import JSONDecodeError

def f1standings(request):
    url = "http://ergast.com/api/f1/2023/driverStandings.json"
    urlTalli = "http://ergast.com/api/f1/2023/constructorStandings.json"
    response = requests.get(url)
    data = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    
    for driver in data:
        constructor_data = driver['Constructors'][0]
        driver['ConstructorName'] = constructor_data['name']
    
    response = requests.get(urlTalli)
    constructor_data = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
    
    return render(request, 'f1/standings.html', {'standings': data, 'constructor_standings': constructor_data})


def races(request):
    round = request.GET.get('round', 1)
    results_url = f'http://ergast.com/api/f1/2023/{round}/results.json'
    try:
        results_data = requests.get(results_url).json()['MRData']['RaceTable']['Races'][0]['Results']
    except (JSONDecodeError, KeyError, IndexError):
        results_data = []
    rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    return render(request, 'f1/races.html', {'results': results_data, 'rounds': rounds, 'selected_round': int(round)})



