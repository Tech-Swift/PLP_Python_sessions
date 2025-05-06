import requests

response = requests.get('https://api.github.com/users/octocat').json()
print(response)
print("User login:", response['login'])