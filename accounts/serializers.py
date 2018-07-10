from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from coins.models import Coin
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    subscription = serializers.StringRelatedField(many=True,
                                                required=False
                                                # slug_field= 'coin',
                                                # queryset=Subscription.objects.all()
                                                )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'subscription')   

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                                validated_data['email'],
                                                validated_data['password'])
        # Assign a new user default top 5 coins 
        default_coins = Coin.objects.order_by('rank')[:5]
        for coin in default_coins:
            # Subscription serializer field for user model is a readonly field so we need to pass that data in save
            default_subscription_serializer = SubscriptionSerializer(data={'coin':coin.slug})
            # validation
            if default_subscription_serializer.is_valid():
                default_subscription_serializer.save(owner=user)
        return user

    # def validate(self, data):
    #     if 'subscription' not in data:
    #         data['subscription'] = ['bitcoin', 'ethereum', 'litecoin']
    #         print(data)
    #         return data
    
