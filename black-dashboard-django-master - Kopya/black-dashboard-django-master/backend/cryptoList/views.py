from django.shortcuts import render


import requests
from django.shortcuts import render

def binance_markets(request):
    url = 'https://api.binance.com/api/v3/ticker/24hr'
    response = requests.get(url)
    markets_data = response.json()

    usd_markets = [market for market in markets_data if market['symbol'].endswith('USDT') or market['symbol'].endswith('USD')]

   
    context = {
        'usd_markets': usd_markets
    }

    return render(request, 'binance_markets.html', context)
