from rocketry import Rocketry
from rocketry.conds import cron
from utils.get_coins.getDolar import get_dolar
from utils.get_coins.getEuro import get_euro
from utils.get_coins.getBitCoin import get_bitcoin
from utils.get_coins.getEthereum import get_ethereum


print("ola mundo")

app = Rocketry()

@app.task(cron("*/2 * * * *"))
def request_coins_values():

    get_dolar()
    get_euro()
    get_bitcoin()
    get_ethereum()

if __name__ == "__main__":
    app.run()