from rest_framework import serializers
from .models import Coin
from datetime import datetime
from django.contrib.auth.models import User

"""serializers
"""
class CoinSerializer(serializers.ModelSerializer):
    """Serializer for the Coin model

    Attributes:
        name (str): coin name ex. btc eth, et cetera.
        ticker (str): shorthand name of the coin
        price (float): latest accessed price from coinmarketcap.com
        last_updated (time): time stamp of last accessed price point
        *update whenever price is updated
        marketcap (float): total market cap of the coin
    """
    class Meta:
        model = Coin
        fields = '__all__'
        lookupfield = "slug"
        # ordering = ('rank',)

        def to_representaiton(self, value):
            value.last_updated = datetime.fromtimestamp(
                value.last_updated).strftime('%Y-%m-%d %H:%M:%S') + 'UTC'


# class UserSerializer(serializers.ModelSerializer):
    


#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username']
#         ),
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
