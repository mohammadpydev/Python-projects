import requests

Headers = {
    "USER-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    "Accept": "image/png"
}

response = requests.get("https://httpbin.org/image", headers=Headers)

with open("mypic.png","wb") as f:
    f.write(response.content)