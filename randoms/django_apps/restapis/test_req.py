import requests

url = 'http://127.0.0.1:8000/auth/hello'
headers = {'Authorization': 'Token 7780b4b32e9c6612b739849b21404fb7fab7b04e'}
response = requests.get(url, headers=headers)

print(response.json())