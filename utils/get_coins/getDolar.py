import requests

def get_dolar():

    print("Pegando valor do dolar")

    try:

        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        dolar_brl = float(dados["USDBRL"]["bid"])

        print(f"1 Dólar (USD) em Reais (BRL): R$ {dolar_brl:.2f}")


    except Exception as e:
        print(f"Erro ao obter valores das moedas: {e}")
