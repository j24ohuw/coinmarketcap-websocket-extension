# Coinmarketcap websocket
API tools and documentation
You can visit the webpage http://j24ohuw.xyz/ for real time data feed on front end


## REST URLs

#### api/coins/available  
- Description: Array of all supported coins
- URL: http://j24ohuw.xyz/api/coins/available
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
- Description: flexible search. Takes a partial or full name, symbol, or slug of a coin and retruns a list of coins with most likely result on top.

- URL: http://j24ohuw.xyz/api/coins/?search=bitcoin
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

    ```
#### api/hist/:symbol 
- Description: Returns up to 300 historical daily values of a coin. 
- URL: http://j24ohuw.xyz/api/hist/BTC
- Response: 
    ```JSON
    {
    "[time, low, high, open, close, volume]": [
        [
            1531267200,
            6282.77,
            6400,
            6303.69,
            6344.51,
            1232.5598331999881
        ],
        [
            1531180800,
            6279,
            6679.47,
            6664.01,
            6303.7,
            8177.853908821869
        ],

    ```
### WebSocket API
- Description: real-time feed of coin data. You must use coin slugs from the availble coin end point above
- URL: ws://j24ohuw.xyz/ws/bitcoin
- Response: 
    ```JSON
    {
        "type": "receive_json", 
        "content": 
            {
                "name": "Bitcoin", 
                "last_updated": 1531282484, 
                "symbol": "BTC", 
                "volume": 4077920000.0, 
                "price": 6378.25, 
                "marketcap": 109340502814.0, 
                "rank": 1, 
                "id": 1, 
                "percent_change_24h": -5.29, 
                "circulating_supply": 17142712.0, 
                "slug": "bitcoin"
            }
    }
    ```

