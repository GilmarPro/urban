import requests

# Include players in teams
r = requests.post('http://127.0.0.1:5000/teams/', data={'player_id': 1, 'team_id': 1})
print(r.text)
r = requests.post('http://127.0.0.1:5000/teams/', data={'player_id': 2, 'team_id': 1})
print(r.text)
r = requests.post('http://127.0.0.1:5000/teams/', data={'player_id': 4, 'team_id': 1})
print(r.text)
r = requests.post('http://127.0.0.1:5000/teams/', data={'player_id': 5, 'team_id': 1})
print(r.text)
r = requests.post('http://127.0.0.1:5000/teams/', data={'player_id': 6, 'team_id': 1})
print(r.text)
r = requests.post('http://127.0.0.1:5000/teams/', data={'player_id': 7, 'team_id': 1})
print(r.text)

# r = requests.post('http://127.0.0.1:5000/teams/', data={'player_id': 2, 'team_id': 2})
# print(r.text)

r = requests.get('http://127.0.0.1:5000/teams/', params={'team_id': 1})
print(r.text)
r = requests.get('http://127.0.0.1:5000/teams/', params={'team_id': 2})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/teams/', data={'player_id': 1, 'team_id': 1})
print(r.text)

r = requests.get('http://127.0.0.1:5000/teams/', params={'team_id': 1})
print(r.text)