import requests


response = requests.get('http://localhost:8000/users?token=jessica', headers={'X-token': 'fake-super-secret-token'})
print(response.text)
