# coinmarketcap-websocket-extension
API tools and documentation



## REST URLs

#### /coins  
- Description: Array of all supported coins
- URL: http://j24ohuw.xyz/api/coins/coin_list
- Response: 
    ```JSON
    [
    "bitcoin",
    "ethereum",
    "ripple",
    "bitcoin-cash",
    "eos",
    "litecoin",
    "stellar",
    "cardano",
    "iota",
    "tether",
    "tron",
    ]

    ```
    
#### /api/coins 
- Description: Current stats of coins shown in table view
- URL: http://j24ohuw.xyz/api/coins
- Response:
    ```JSON
    {
    "count": 1628,
    "next": "http://127.0.0.1:8000/api/coins/?limit=100&offset=100",
    "previous": null,
    "results": [
        {
            "id": 1,
            "circulating_supply": 17140762.0,
            "name": "Bitcoin",
            "symbol": "BTC",
            "price": 6753.81,
            "last_updated": 1531187006.0,
            "marketcap": 115765449803.0,
            "volume": 3714850000.0,
            "slug": "bitcoin",
            "rank": 1,
            "percent_change_24h": -0.16
        },
                {
            "id": 1027,
            "circulating_supply": 100592953.0,
            "name": "Ethereum",
            "symbol": "ETH",
            "price": 476.901,
            "last_updated": 1531187011.0,
            "marketcap": 47972880042.0,
            "volume": 1553590000.0,
            "slug": "ethereum",
            "rank": 2,
            "percent_change_24h": -2.08
        },
 
    ```
#### /api/coins/?search=:coin  
- Description: flexible search. Takes partial or full name, symbol, slug, ID of an individual coin, and retruns list of coins, most likely result on top.

- URL: http://j24ohuw.xyz/api/?search=bitcoin
    ```JSON
    {
    "count": 32,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "circulating_supply": 17140762.0,
            "name": "Bitcoin",
            "symbol": "BTC",
            "price": 6753.81,
            "last_updated": 1531187006.0,
            "marketcap": 115765449803.0,
            "volume": 3714850000.0,
            "slug": "bitcoin",
            "rank": 1,
            "percent_change_24h": -0.16
        },
        {
            "id": 1831,
            "circulating_supply": 17228950.0,
            "name": "Bitcoin Cash",
            "symbol": "BCH",
            "price": 733.651,
            "last_updated": 1531187014.0,
            "marketcap": 12640036396.0,
            "volume": 341154000.0,
            "slug": "bitcoin-cash",
            "rank": 4,
            "percent_change_24h": -2.17
        },
        {...
