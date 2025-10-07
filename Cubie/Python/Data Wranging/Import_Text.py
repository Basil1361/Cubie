# pip install requests
import requests

url = "https://jsonplaceholder.typicode.com/todos"
resp = requests.get(url, timeout=15)
data = resp.json()

print(data)
