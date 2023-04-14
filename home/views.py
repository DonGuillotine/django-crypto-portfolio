from django.shortcuts import render
import requests
from pycoingecko import CoinGeckoAPI

# Render home page
def index(request):
    cg = CoinGeckoAPI()
    top_currencies = cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page=10)
    return render(request, 'home.html')