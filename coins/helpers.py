import urllib.request, json
import pandas as pd
from datetime import datetime
import gdax
public_client = gdax.PublicClient()

#import numpy as np
BASE_URL = 'https://api.coinmarketcap.com/v2/'
LAST_UPDATED = -1

def get_num_currencies():
    with urllib.request.urlopen(BASE_URL+'listings/') as url:
        try:
            metadata = json.loads(url.read().decode())['metadata']
            count = metadata['num_cryptocurrencies']
            return count
        except Exception as e:
            print(e.message, e.args)

def parser(data):
    for key in data.keys():
        replace = {}
        replace['price'] = data[key]['quotes']['USD']['price']
        replace['volume'] = data[key]['quotes']['USD']['volume_24h']
        replace['marketcap'] = data[key]['quotes']['USD']['market_cap']
        replace['percent_change_24h'] = data[key]['quotes']['USD']['percent_change_24h']
        replace['symbol'] = data[key]['symbol']
        replace['id'] = data[key]['id']
        replace['name'] = data[key]['name']
        replace['circulating_supply'] =data[key]['circulating_supply']
        replace['last_updated'] = data[key]['last_updated']
        replace['slug'] = data[key]['website_slug']
        replace['rank'] = data[key]['rank']
        data[key] = replace
        # print(data)
    return data

def get_coin_data(start=0, limit=100):
    finish = start + limit -1
    # print('Getting tickers (sorted by rank) from {start:d} to {finish:d}'
    #         .format(start=start, finish=finish))

    with urllib.request.urlopen(
        BASE_URL+'ticker/?start=' + str(start) + '&limit=' + str(limit)
        ) as url:
        print(url)
        data =json.loads(url.read().decode())['data']
        # print(data)
    return parser(data)

def get_daily_data(symbol):
    request_str = symbol + '-USD'
    # set granularity to a day = 86400 seconds
    data = public_client.get_product_historic_rates(request_str,granularity=86400)
    # url = ALPHA_VANTAGE_DAILY_URL + symbol
    # url = 'https://api.pro.coinbase.com/products/'+symbol+'-usd/candles'
    # print(url)
    # data = requests.get(url).json()
    return data


# def get_listings():
#     print('get_listings called')
#     with urllib.request.urlopen(BASE_URL+'listings/') as url:
#         try:
#             data = json.loads(url.read().decode())['data']
#             # for coin in data:
#                 # IDs.add(coin['id'])
#                 # names.add(coin['name'])
#                 # symbols.add(coin['symbol'])
#             # return return_vals IDs, names, symbols
#         except:
#             print('exception occurred at get_listings')
#             # raise BaseException
#
# def get_coin_data(id):
#     print('get_coin_data called', id)
#     #return price, float, volume, marketcap, last_updated
#     with urllib.request.urlopen(BASE_URL+'ticker/'+ str(id)) as url:
#         return_vals = {'price':-1,
#                         'float': -1,
#                         'volume': -1,
#                         'marketcap': -1,
#                         'last_updated': -1}
#         try:
#             data = json.loads(url.read().decode())['data']
#             return_vals['name'] = data['quotes']['name']
#             return_vals['symbol'] = data['quotes']['symbol']
#             return_vals['API_ID'] = data['quotes']['id']
#             return_vals['price'] = data['quotes']['USD']['price']
#             return_vals['float'] = data['total_supply']
#             return_vals['volume'] = data['quotes']['USD']['volume_24h']
#             return_vals['marketcap'] = data['quotes']['USD']['market_cap']
#             return_vals['last_updated'] = data['quotes']['last_updated']
#             return return_vals
#         except:
#             print('error occurred at get_coin_data')
