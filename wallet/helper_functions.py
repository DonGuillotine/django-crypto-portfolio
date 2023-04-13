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