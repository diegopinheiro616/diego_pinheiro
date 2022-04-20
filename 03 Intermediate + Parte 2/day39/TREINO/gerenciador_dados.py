import requests

SHEETY_PRECOS_ENDPOINT = "https://api.sheety.co/2ca1b0d11e6e3fdba128a4f85418b9e8/flightDeals2/sheet1"
APP_ID = "f0b386d9"
API_KEY = "4808a0931b46b5914adbd27ae3ed2b55"
BEARER_AUTHENTIFICATION = "3:qk>+tEmS$>n7N"
"""
sheety_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
"""
sheety_bearer_authorization = {
    "Authorization": f"Bearer {BEARER_AUTHENTIFICATION}"
}


class GerenciadorDados:

    def __init__(self):
        self.destino_dados = {}

    def pegar_destino_dados(self):

        resposta = requests.get(url=SHEETY_PRECOS_ENDPOINT, headers=sheety_bearer_authorization)
        dados = resposta.json()
        # print(dados)
        # {'sheet1': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 1000, 'id': 2},
        # {'city': 'Wellington', 'iataCode': '', 'lowestPrice': 1000, 'id': 3}]}
        self.destino_dados = dados["sheet1"]  # <---- "sheet1" é o nome do diretorio que está o sheet Flight Deals 2
        # print(self.destino_dados)
        # [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 1000, 'id': 2},
        # {'city': 'Wellington', 'iataCode': '', 'lowestPrice': 1000, 'id': 3}]
        return self.destino_dados

    def atualizar_destino_dados(self):

        for city in self.destino_dados:
            novo_dado = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            resposta = requests.put(
                url=f"{SHEETY_PRECOS_ENDPOINT}/{city['id']}",
                json=novo_dado,
                headers=sheety_bearer_authorization
            )
            print(resposta.text)
            #   " [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 1000, 'id': 2}, "
            #  "{'city': 'Wellington', 'iataCode': 'WLG', 'lowestPrice': 1000, 'id': 3}]")
            # {
            #   "sheet1": {
            #     "iataCode": "PAR",
            #     "id": 2
            #   }
            # }
            # {
            #   "sheet1": {
            #     "iataCode": "WLG",
            #     "id": 3
            #   }
            # }