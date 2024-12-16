import requests

def get_bitcoin():
    print("Pegando valor do Bitcoin")

    try:
        url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        bitcoin_brl = float(dados["BTCBRL"]["bid"])

        print(f"1 Bitcoin (BTC) em Reais (BRL): R$ {bitcoin_brl:,.2f}")

    except Exception as e:
        print(f"Erro ao obter valor do Bitcoin: {e}")
