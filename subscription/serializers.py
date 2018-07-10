from rest_framework import serializers
from .models import Subscription
from coins.models import Coin

"""serializers
"""
class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for the Subscriber model"""
    owner = serializers.ReadOnlyField(source='owner.username')

    coin = serializers.SlugRelatedField(slug_field='slug',
                                        queryset=Coin.objects.all()
                                        )
    class Meta:
        model = Subscription
        fields = ('owner', 'coin','id')


# lookup_field = 'coin__slugs'
# slug = serializers.SlugRelatedField(
#     many=False,
#     read_only=True,
#     slug_field='slug',
# )
# owner = serializers.StringRelatedField(read_only=True)
