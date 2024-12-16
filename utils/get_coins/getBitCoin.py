from connections.apiCoins import api_coins

def get_bitcoin():
    print("Pegando valor do Bitcoin")

    try:
        coin = "BTC-BRL"
        dados = api_coins(coin)
        bitcoin_brl = float(dados["BTCBRL"]["bid"])

        print(f"1 Bitcoin (BTC) em Reais (BRL): R$ {bitcoin_brl:,.2f}")

    except Exception as e:
        print(f"Erro ao obter valor do Bitcoin: {e}")
