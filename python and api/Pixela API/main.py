import requests
from datetime import datetime


TOKEN = "xxxxxxxxx"
USERNAME = "xxxx"
GRAPHID = "xxxx"
today = datetime.now()
d_time = today.strftime("%Y%m%d")

###########################################
##########         post          ##########
###########################################

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

###########################################
##########         post          ##########
###########################################

gragh_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "100 day of python",
    "unit": "day",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=gragh_endpoint, json=graph_config, headers=headers)
print(response.text)

###########################################
##########         post          ##########
###########################################

records_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"


records_params = {
    "date": d_time,
    "quantity": input("how many days did you complete today!")
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=records_endpoint, json=records_params, headers=headers)
print(response.text)

###########################################
##########         put           ##########
###########################################

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{d_time}"
update_config = {
    "quantity": "5",
 }
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

###########################################
##########        delete         ##########
###########################################

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{d_time}"
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url=delete_endpoint, headers=headers)

