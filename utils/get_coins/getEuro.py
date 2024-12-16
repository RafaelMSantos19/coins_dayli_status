from connections.apiCoins import api_coins

def get_euro():

    print("Pegando valor do euro")

    try:
        coin = "EUR-BRL"
        dados = api_coins(coin)
        euro_brl = float(dados["EURBRL"]["bid"])

        print(f"1 Euro (EUR) em Reais (BRL): R$ {euro_brl:.2f}")

    except Exception as e:
        print(f"Erro ao obter valores das moedas: {e}")

