from rest_framework import serializers
from .models import Subscription
from coins.models import Coin

"""serializers
"""
class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for the Subscriber model"""

    class Meta:
        model = Subscription
        fields = ('owner', 'coin','id')


