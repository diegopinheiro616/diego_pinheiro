from pprint import pprint
from datetime import datetime, timedelta
from gerenciador_dados import GerenciadorDados
from procurar_viagem import ProcurarViagem
from gerenciador_notificacao import GerenciadorNotificacao

gerenciador_dados = GerenciadorDados()
procurar_viagem = ProcurarViagem()
gerenciador_notificacao = GerenciadorNotificacao()

sheet_dados = gerenciador_dados.pegar_destino_dados()

CIDADE_SAIDA_IATA = "GRU"

amanha_sem_formatacao = datetime.now() + timedelta(days=1)
AMANHA = amanha_sem_formatacao.strftime("%d/%m/%Y")
daqui_seis_meses_sem_formatacao = datetime.now() + timedelta(days=6*30)
SEIS_MESES = daqui_seis_meses_sem_formatacao.strftime("%d/%m/%Y")

if sheet_dados[0]["iataCode"] == "":
    for row in sheet_dados:
        row["iataCode"] = procurar_viagem.pegar_destino_codigo(row["city"])
    pprint(f"sheet_dados:\n {sheet_dados}")
    gerenciador_dados.destino_dados = sheet_dados
    gerenciador_dados.atualizar_destino_dados()

for destino in sheet_dados:
    voo = procurar_viagem.verificar_voo(
        CIDADE_SAIDA_IATA,
        destino["iataCode"],
        inicio_tempo=AMANHA,
        final_tempo=SEIS_MESES,
    )
    if voo is not None and voo.preco < destino["lowestPrice"]:
        gerenciador_notificacao.mandar_msn(
            mensagem=f"Alerta de preço 'BAIXO'! Bagatela de R${voo.preco} para voar de {voo.cidade_origem}/"
                     f"{voo.aeroporto_origem} para {voo.cidade_destino}/{voo.aeroporto_destino}, de {voo.data_saida}"
                     f"até {voo.data_retorno}."
        )
