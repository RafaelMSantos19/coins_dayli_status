from datetime import datetime
from rocketry import Rocketry
from rocketry.conds import cron
from utils.get_coins.getDolar import get_dolar
from utils.get_coins.getEuro import get_euro
from utils.get_coins.getBitCoin import get_bitcoin
from utils.get_coins.getEthereum import get_ethereum

print("Start")

app = Rocketry()

@app.task(cron("* * * * *"))
def request_coins_values():

    try:

        coins_tuple = {
            "Dolar": get_dolar(),
            "Euro": get_euro(),
            "Bitcoin": get_bitcoin(),
            "Ethereum": get_ethereum()
        }


        print(datetime.now())
        
        print(coins_tuple)

    except Exception as e:

        print(f"falha causado por: {e}")

#create function to send data to database

#create function to send report to email 

if __name__ == "__main__":
    app.run()