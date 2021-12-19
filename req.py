import requests

r = requests.post('http://127.0.0.1:5000/player/', data={'name': 'Gilmar'})
# r = requests.get('http://127.0.0.1:5000/player/', params={'id': 1})
# r = requests.get('http://127.0.0.1:5000/player/')
# r = requests.delete('http://127.0.0.1:5000/player/', params={'id': 10})
# r = requests.put('http://127.0.0.1:5000/player/', data={'id': 11, 'name': 'Ricarth'})
                                                        
r.raise_for_status()

print(r.text)