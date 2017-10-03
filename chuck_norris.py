import requests

r = requests.get('http://api.icndb.com/jokes/random/')

data = r.json()
print(data)
print(data['value']['id'])
print(data['value']['joke'])
