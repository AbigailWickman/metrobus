import requests

r = requests.get("http://localhost:5000/server")
print(r.text)
