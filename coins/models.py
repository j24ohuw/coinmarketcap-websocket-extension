from django.db import models
from django.utils import timezone

"""Todo:
"""

class Coin(models.Model):
    """Simple cryptocurrency model
    Attributes:
        name (str): coin name ex. btc eth, et cetera.
        ticker (str): shorthand name of the coin
        price (float): latest accessed price from coinmarketcap.com
        last_updated (time): time stamp of last accessed price point
        *update whenever price is updated
        market_cap (float): total market cap of the coin
    """
    circulating_supply = models.FloatField(default=-1,
                                null=True,
                                blank=True)
    name = models.CharField(default='', 
                                max_length = 100)
    symbol = models.CharField(default='', 
                                max_length = 100)
    id = models.IntegerField(default=-1, 
                                primary_key=True)# API_ID
    price = models.FloatField(default=-1,
                                null=True,
                                blank=True)
    last_updated = models.FloatField(default=-1, 
                                null=True,
                                blank=True)
    marketcap = models.FloatField(default=-1,
                                null=True,
                                blank=True)
    volume = models.FloatField(default=-1,
                                null=True,
                                blank=True)
    slug = models.CharField(default='', 
                                max_length=100,
                                null=True,
                                blank=True)
    rank = models.IntegerField(default=-1,
                                null=True,
                                blank=True)
    percent_change_24h = models.FloatField(default = 0,
                                null=True,
                                blank=True)

    def __unicode__(self):
        return self.name