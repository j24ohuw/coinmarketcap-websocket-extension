# import urllib.request, json
# import pandas as pd
# BASE_URL = 'https://api.coinmarketcap.com/v2/'
# id = 1
# print('get_listings called')
# with urllib.request.urlopen(BASE_URL+'ticker/') as url:
#         data = json.loads(url.read().decode())['data']
#         df = pd.DataFrame(data = data).T

#         for i, quote in enumerate(df['quotes']):
#             df.loc[df.index[i],'price'] = quote['USD']['price']
#             df.loc[df.index[i],'volume'] = quote['USD']['volume_24h']
#             df.loc[df.index[i],'market_cap'] = quote['USD']['market_cap']
#         df['float'] = df['circulating_supply']
# ##        df['last_updated'] = pd.to_datetime(df['last_updated'],unit='s')
#         drop_list = ['quotes','website_slug', 'max_supply','rank', 'circulating_supply', 'total_supply']
#         df = df.drop(columns=drop_list)
    
