import requests
from datetime import date, time

# r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Gilmar', 'mail': 'gilmar@gmail.com'})
# r = requests.get('http://127.0.0.1:5000/players/', params={'id': 1})
# r = requests.get('http://127.0.0.1:5000/players/')
# r = requests.delete('http://127.0.0.1:5000/players/', params={'id': 10})
# r = requests.put('http://127.0.0.1:5000/players/', data={'id': 11, 'name': 'Ricarth'})

# Match : Rue des Erables, 31/12/2021, 15:00
address = 'Rue des Erables'
day = '31-12-2021'
hour = '15:00'
# r = requests.post('http://127.0.0.1:5000/matches/', data={'address': address, 'day': day, 'hour': hour})

r = requests.post('http://127.0.0.1:5000/matches/add_player', data={'player_id': 1, 'team_id': 2})

r.raise_for_status()

print(r.text)