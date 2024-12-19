from connections.apiCoins import api_coins

def get_bitcoin():

    try:
        coin = "BTC-BRL"
        dados = api_coins(coin)
        bitcoin_brl = float(dados["BTCBRL"]["bid"])

        return bitcoin_brl

    except Exception as e:
        print(f"Erro ao obter valor do Bitcoin: {e}")
