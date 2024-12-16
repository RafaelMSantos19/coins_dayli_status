import requests


def api_coins(coin):

        try:
                url = f"https://economia.awesomeapi.com.br/json/last/{coin}"
                return requests.get(url).json()
        
        except Exception as e:
                print(f"Erro ao fazer a request para api coins: {e}")


