from connections.apiCoins import api_coins

def get_euro():

    try:
        coin = "EUR-BRL"
        dados = api_coins(coin)
        euro_brl = float(dados["EURBRL"]["bid"])

        return euro_brl

    except Exception as e:
        print(f"Erro ao obter valores das moedas: {e}")

