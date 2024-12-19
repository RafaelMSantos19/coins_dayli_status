from connections.apiCoins import api_coins

def get_dolar():

    try:

        coin = "USD-BRL"
        dados = api_coins(coin)
        dolar_brl = float(dados["USDBRL"]["bid"])

        return dolar_brl

    except Exception as e:
        print(f"Erro ao obter valores das moedas: {e}")

