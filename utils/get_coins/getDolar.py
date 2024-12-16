from connections.apiCoins import api_coins

def get_dolar():
    print("Pegando valor do dolar")

    try:

        coin = "USD-BRL"
        dados = api_coins(coin)
        dolar_brl = float(dados["USDBRL"]["bid"])

        print(f"1 Dólar (USD) em Reais (BRL): R$ {dolar_brl:.2f}")


    except Exception as e:
        print(f"Erro ao obter valores das moedas: {e}")

