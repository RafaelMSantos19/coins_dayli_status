import requests

def get_ethereum():
    print("Pegando valor do Ethereum")

    try:
        url = "https://economia.awesomeapi.com.br/json/last/ETH-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        ethereum_brl = float(dados["ETHBRL"]["bid"])

        print(f"1 Ethereum (ETH) em Reais (BRL): R$ {ethereum_brl:,.2f}")

    except Exception as e:
        print(f"Erro ao obter valor do Ethereum: {e}")
