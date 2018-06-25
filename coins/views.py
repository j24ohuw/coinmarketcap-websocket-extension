import datetime
import pandas as pd
from time import time
#core django
from django.http import Http404
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe
# from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
#third party
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
#my apps
from .models import Coin
from .serializers import CoinSerializer

from .helpers import get_num_currencies
from .tasks import *
# from .tasks import renew_database
# LISTING_DF = get_listings()
"""Provide list, retrieve, get_detail, update, and create views
"""

def tableView(request):
    return render(request, 'coins/table.html', {})

def coin_detail(request):
    return render(request, 'coins/coin_detail.html', {})


def index(request):
    return render(request, 'coins/index.html', {})

import json
def room(request, room_name):
    return render(request, 'coins/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all().order_by('rank')
    serializer_class = CoinSerializer
    # search filter; allows searching coins with name, symbol, or ID
    # http://127.0.0.1:8000/api/coins/?search=1027
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', '=id', 'symbol',)


class CoinSearchListVIew(ListAPIView):
    """
    Display list filtered by search query.
    """
    queryset = Coin.objects.all().order_by('rank')
    serializer_class = CoinSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('=id','name', 'symbol',)

    # def get_queryset(self):
    #     keywords = self.request.GET.get('q')
        
    #     if keywords:
    #         query = SearchQuery(keywords)
    #         vector = SearchVector('id', 'name', 'symbol')
    #         qs = self.queryset.filter(search=query)
    #         qs = qs.annotate(rank=SearchRank(vector, query)).order_by('-rank')
    #     return qs



















# class CoinView(viewsets.ModelViewSet):
#     #default queryset to all coin objects
#     queryset = Coin.objects.all()
#     serializer_class = CoinSerializer
    
#     def get_last_updated(self):
#         BTC = self.queryset.filter(name='Bitcoin').first()
#         serializer = self.get_serializer(BTC)
#         return serializer.data['last_updated']

#     def add_coins(self, request):
#         #compile a list of coin IDs
#         print('add_coins')
#         for API_ID in LISTING_DF['API_ID']:
#             self.create(request, API_ID)
#         # serializer = self.get_serializer(self.queryset, many=True)
#         # return Response(serializer.data, many=True)

#     #call 
#     def list(self, request):
#         # check empty queryset
#         if len(self.queryset) == 0:
#             #initiate and add coin data
#             self.add_coins(request) # refactor it with is_complete()
        
#         # Check if last_updated timestamp is within 5 minutes of the current time
#         # 5 minutes difference is 300 in unix timestamp (or 300.000)
#         if time() - self.get_last_updated() >= 300:
#             LISTING_DF = get_listings()
#             for coin in Coin.objects.all():
#                 print(coin.API_ID)
#                 self.update(request, coin.API_ID)

#         # if the above didn't execute then we just need to return response
#         # if it did, the data is up-to date.
#         objs = Coin.objects.all()
#         serializer = self.get_serializer(objs, many=True)
#         return Response(serializer.data)

#     """create is called to add all new coins to the database"""
#     def create(self, request, API_ID):
#         # get corresponding slice of DF to data var
#         data = LISTING_DF[API_ID == LISTING_DF['API_ID']]
#         data = data.to_dict(orient = 'records')[0]
#         print(data)
#         # data is passed in as a dict format
#         coin = Coin(API_ID=API_ID)
#         serializer = self.get_serializer(coin, data=data)
#         print(len(self.queryset.filter(API_ID=API_ID)))
#         if serializer.is_valid() and \
#             len(self.queryset.filter(API_ID=API_ID)) == 0:
#             serializer.save()
#             # return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     #new coin to update
#     def update(self, request, API_ID):
#         #setup
#         #TODO Protect get_listings from getting called too many  times
#         data_df = LISTING_DF#get_listings() #listing data in pandas dataframe
#             # print(coin['API_ID'] in set(data_df['API_ID']))
#             # update the coins in the current database 
#             # get the coin data from DataFrame and update
#         if API_ID in set(data_df['API_ID']):
#             # print(self.queryset.filter(API_ID=coin['API_ID']).values())
#             query = get_object_or_404(self.queryset, API_ID=API_ID)
#             data = data_df[data_df['API_ID']==API_ID]
#             # get a flat dictionary
#             data = data.to_dict(orient='records')[0]
#             # print(data)         
#             serializer = self.get_serializer(query, data=data)
#             if serializer.is_valid():
#                 print(data['name'], ' updated')
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 print('Bad request  raised at update_data')
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, API_ID, data):
#         pass
    
#     # destroy if removed from the coinmarketcap listings/exchange
#     def destroy(self, request, pk=None):
#         pass


