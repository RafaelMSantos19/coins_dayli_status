import requests

def get_euro():

    print("Pegando valor do euro")

    try:

        url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        euro_brl = float(dados["EURBRL"]["bid"])

        print(f"1 Euro (EUR) em Reais (BRL): R$ {euro_brl:.2f}")

    except Exception as e:
        print(f"Erro ao obter valores das moedas: {e}")

