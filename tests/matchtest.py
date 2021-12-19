import requests

# Create matches
address = 'Rue des Erables'
day = '31-12-2021'
hour = '15:00'
r = requests.post('http://127.0.0.1:5000/matches/', data={'address': address, 'day': day, 'hour': hour})
print(r.text)

address = 'Rue Bleue'
day = '01-12-2021'
hour = '12:00'
r = requests.post('http://127.0.0.1:5000/matches/', data={'address': address, 'day': day, 'hour': hour})
print(r.text)

address = 'Rue des Champs'
day = '04-01-2022'
hour = '09:15'
r = requests.post('http://127.0.0.1:5000/matches/', data={'address': address, 'day': day, 'hour': hour})
print(r.text)

# Read all available matches
r = requests.get('http://127.0.0.1:5000/matches/')
print(r.text)

# Update a match
address = 'Crumpsall Street'
day = '25-02-2022'
hour = '11:45'
r = requests.put('http://127.0.0.1:5000/matches/', data={'id': 1, 'address': address, 'day': day, 'hour': hour})
print(r.text)

# Read all available matches
r = requests.get('http://127.0.0.1:5000/matches/')
print(r.text)

# Delete a match
r = requests.put('http://127.0.0.1:5000/matches/', params={'id': 3})

# Read all available matches
r = requests.get('http://127.0.0.1:5000/matches/')
print(r.text)

# Read one match
r = requests.get('http://127.0.0.1:5000/matches/', params={'id': 1})
print(r.text)