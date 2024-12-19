from connections.apiCoins import api_coins

def get_ethereum():

    try:
        coin = "ETH-BRL"
        dados = api_coins(coin)
        ethereum_brl = float(dados["ETHBRL"]["bid"])
        
        return ethereum_brl

    except Exception as e:
        print(f"Erro ao obter valor do Ethereum: {e}")
