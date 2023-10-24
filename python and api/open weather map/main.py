import requests

link = "https://api.openweathermap.org/data/2.5/weather"

key_api = "8fad155383c58b2ef41619449b022efb"


Parameters = {
    "lat" : 35.881930,
    "lon": 37.349777,
    "appid": key_api,
    "units": "metric",
    "lang": "ar"

}

response = requests.get(url=link, params=Parameters)
response.raise_for_status()
# Handling Response Content
data = response.json()
print(data)
# Get the temperature in Celsius
temp = data["main"]["temp"]
print(temp)
