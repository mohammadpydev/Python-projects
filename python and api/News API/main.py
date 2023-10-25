import requests

link = "https://newsapi.org/v2/everything"

key_api = "0f8745c80782467689db00577be47930"


Parameters = {
    "q": "bitcoin",
    "apiKey": key_api,
    "language": "en",
}

response = requests.get(url=link, params=Parameters)
response.raise_for_status()
# Handling Response Content
data = response.json()
# Get news title
title = []
for i in range(0, len(data["articles"])):
    title.append(data["articles"][i]["title"])

print(title)
