# Clash Royale Public API ilə oyunçu datası (Python)

import requests

API_KEY = 'Bearer YOUR_API_TOKEN'
BASE    = 'https://api.clashroyale.com/v1'

def get_player(player_tag):
    tag = player_tag.replace('#', '%23')
    url = f'{BASE}/players/{tag}'
    headers = {'Authorization': API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

def get_top_players():
    url = f'{BASE}/locations/global/rankings/players'
    headers = {'Authorization': API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()['items']

# İstifadə nümunəsi
player = get_player('#2PP')
print(player['name'], player['trophies'])
