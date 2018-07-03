from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, serializers, status
from rest_framework.response import Response
from coins.models import Coin
from .models import Subscription
from .serializers import SubscriptionSerializer
from .permissions import IsOwnerOrReadOnly
# from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          )
    lookup_field = 'coin__slug'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            self.user = user
            return Subscription.objects.filter(owner=user)
        else:
            return Subscription.objects.filter(owner=None)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # def destroy(self, request, slug): #format=None
    #     queryset = self.get_queryset()
    #     print(request)
    #     obj = queryset.get_object(coin=slug)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

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
