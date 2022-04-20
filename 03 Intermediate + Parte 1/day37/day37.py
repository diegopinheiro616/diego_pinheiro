""" Day 37 """

# ######### HTTP Post Requests ###########

# Tipos de HTTP Requests: Get: "requests.get()", Post, Put, Delete (igual o primeiro "requests.put()")
# Post(postar), Put(Atualizar), Delete (deletar)
# Habit Tracker

import requests
from datetime import datetime

USERNAME = "ninesagesrpg"
TOKEN = "08Lev:28ram"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # Sucess creating username/token

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)    # {"message":"Success.","isSuccess":true}

# https://pixe.la/v1/users/ninesagesrpg/graphs/graph1.html  <---- Ver o gráfico

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()  # <---- identifica automaticamente o dia
# print(today)  # 2022-01-05 10:35:25.584832
# print(today.strftime("%Y%m%d"))  # <---- "strftime("%Y%m%d")" reconfigura a data.. nesse caso opção "%Y" + "%m" + "%d"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

# today = datetime(year=2022, month=1, day=4)

# pixel_data = {
#    "date": today.strftime("%Y%m%d"),
#    "quantity": "2.00",
#}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)  # {"message":"Success.","isSuccess":true}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "3.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)