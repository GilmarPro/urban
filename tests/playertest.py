import requests

# Create players
r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Gilmar', 'mail': 'gilmar@gmail.com'})
print(r.text)
r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Albino', 'mail': 'albino@gmail.com'})
print(r.text)
r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Santos', 'mail': 'santos@gmail.com'})
print(r.text)
r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Ana', 'mail': 'ana@gmail.com'})
print(r.text)
r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Bia', 'mail': 'bia@gmail.com'})
print(r.text)
r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Melo', 'mail': 'melo@gmail.com'})
print(r.text)
r = requests.post('http://127.0.0.1:5000/players/', data={'name': 'Ian', 'mail': 'ian@gmail.com'})
print(r.text)

# Read all players
r = requests.get('http://127.0.0.1:5000/players/')
print(r.text)
# Read one player
r = requests.get('http://127.0.0.1:5000/players/', params={'id': 1})
print(r.text)

# Update one player
r = requests.put('http://127.0.0.1:5000/players/', data={'id': 1, 'name': 'Junior', 'mail': 'junior@gmail.com'})
print(r.text)

# Read all players
r = requests.get('http://127.0.0.1:5000/players/')
print(r.text)

# Delete one player
r = requests.delete('http://127.0.0.1:5000/players/', params={'id': 3})
print(r.text)

# Read all players
r = requests.get('http://127.0.0.1:5000/players/')
print(r.text)