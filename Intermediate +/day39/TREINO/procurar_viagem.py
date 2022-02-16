import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "PSoCekQsDNr91wbFofy9HjMRsAsjsXfz"

Afiliaca_ID = "9sagesrpgflightsearch"

amanha_sem_formatacao = datetime.now() + timedelta(days=1)
AMANHA = amanha_sem_formatacao.strftime("%d/%m/%Y")
daqui_seis_meses_sem_formatacao = datetime.now() + timedelta(days=6*30)
SEIS_MESES = daqui_seis_meses_sem_formatacao.strftime("%d/%m/%Y")


class DadosViagem:

    def __init__(self, preco, cidade_origem, aeroporto_origem, cidade_destino,
                 aeroporto_destino, data_saida, data_retorno):
        self.preco = preco
        self.cidade_origem = cidade_origem
        self.aeroporto_origem = aeroporto_origem
        self.cidade_destino = cidade_destino
        self.aeroporto_destino = aeroporto_destino
        self.data_saida = data_saida
        self.data_retorno = data_retorno


class ProcurarViagem:

    @staticmethod
    def pegar_destino_codigo(nome_cidade):

        localizacao_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        solicitacao = {"term": nome_cidade, "localion_types": "city"}
        resposta_pegar_destino = requests.get(url=localizacao_endpoint, headers=headers, params=solicitacao)
        resultado_pegar_destino = resposta_pegar_destino.json()["locations"]
        print(f"resultado_codigo abaixo {resultado_pegar_destino}")
        code = resultado_pegar_destino[0]["code"]
        return code

    @staticmethod
    def verificar_voo(codigo_cidade_origem, codigo_cidade_destino, inicio_tempo, final_tempo):
        headers = {"apikey": TEQUILA_API_KEY}
        pedido_verificar_voo = {
            "fly_from": codigo_cidade_origem,
            "fly_to": codigo_cidade_destino,
            "date_from": inicio_tempo,
            "date_to": final_tempo,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "BRL"
        }
        resposta_pedido_verificar_voo = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=pedido_verificar_voo,
        )

        try:
            dados_pedido_verificar_voo = resposta_pedido_verificar_voo.json()["data"][0]
        except IndexError:
            print(f"Não foi encontrado nenhum voo para {codigo_cidade_destino}.")
            return None

        dados_voo = DadosViagem(
            preco=dados_pedido_verificar_voo["price"],
            cidade_origem=dados_pedido_verificar_voo["route"][0]["cityFrom"],
            aeroporto_origem=dados_pedido_verificar_voo["route"][0]["flyFrom"],
            cidade_destino=dados_pedido_verificar_voo["route"][0]["cityTo"],
            aeroporto_destino=dados_pedido_verificar_voo["route"][0]["flyTo"],
            data_saida=dados_pedido_verificar_voo["route"][0]["local_departure"].split("T")[0],
            data_retorno=dados_pedido_verificar_voo["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{dados_voo.cidade_destino}: R${dados_voo.preco}")
        return dados_voo
