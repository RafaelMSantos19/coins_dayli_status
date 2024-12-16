from connections.apiCoins import api_coins

def get_ethereum():
    print("Pegando valor do Ethereum")

    try:
        coin = "ETH-BRL"
        dados = api_coins(coin)
        ethereum_brl = float(dados["ETHBRL"]["bid"])

        print(f"1 Ethereum (ETH) em Reais (BRL): R$ {ethereum_brl:,.2f}")

    except Exception as e:
        print(f"Erro ao obter valor do Ethereum: {e}")
