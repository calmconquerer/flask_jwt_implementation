import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(url=BASE + "user")
print(response.json())