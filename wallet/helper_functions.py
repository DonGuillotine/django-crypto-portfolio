import requests
from pycoingecko import CoinGeckoAPI
import json


#  Get Coin List from CoinGeckoAPI
def get_coin_list():
    cg = CoinGeckoAPI()
    coin_list = list(((f"{coin['id']} ({coin['symbol'].upper()})") for coin in cg.get_coins_list()))
    return coin_list


#  Get price
def get_price(coin_id):
    cg = CoinGeckoAPI()
    return cg.get_price(ids=coin_id, vs_currencies="usd")[coin_id]["usd"]


#   Retrieves the latest Fear and Greed Index (FGI) value from the Alternative.me API
def get_fg(classification=False):
    fg = requests.get("https://api.alternative.me/fng/").json().get("data")[0]


    #  Returns either the FGI numerical value or classification based on the classification parameter.
    if not classification:
        return fg['value']
    else:
        return fg['value_classification']