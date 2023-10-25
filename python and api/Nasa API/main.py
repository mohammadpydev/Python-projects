import requests

link = "https://api.nasa.gov/DONKI/FLR"

key_api = "gJRDOs5QGMaxikecjHp98MObc4wOpfM1PHwjsL4T"


Parameters = {
    "startDate": "2023-01-01",
    "endDate": "2023-01-30",
    "api_key": "gJRDOs5QGMaxikecjHp98MObc4wOpfM1PHwjsL4T"
}

response = requests.get(url=link, params=Parameters)
response.raise_for_status()
# Handling Response Content
data = response.json()
print(data)