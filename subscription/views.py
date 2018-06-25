from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, serializers, status
from rest_framework.response import Response
from coins.models import Coin
from .models import Subscription
from .serializers import SubscriptionSerializer
from .permissions import IsOwnerOrReadOnly
# from .serializers import UserSerializer

class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          )
    
    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(owner=user)
    
    
    # def create(self, request):
    #     print(request.data['coin'])
    #     print(self.queryset.filter(coin=request.data['coin']))
    #     print(self.queryset.get(coin=request.data['coin']))
    #     print(self.queryset == self.get_queryset())

        
        # if request.data['coin'] in self.queryset()
    # def coin_query(self, API_ID):

    #     coin = Coin.get_object(API_ID=API_ID)
    #     # if len(coin) > 1:
    #     #     print('More than one instance of coin #', API_ID)
    #     return coin
    
    # # Take Coinmarketcap API_ID key as an input
    # def create(self, request, API_ID):
    #     coin = self.coin_query(API_ID)
    #     serializer = self.get_serializer(coin=coin, owner=requ
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     # validate and save
    # def destroy(self, request, API_ID):
    #     coin = self.coin_query(API_ID)
    #     selected_subscription = self.get_queryset().filter(coin=coin)
    #     selected_subscription.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
