from __future__ import absolute_import, unicode_literals
import os, time, json
from datetime import datetime, timedelta
from math import ceil
from celery.utils.log import get_task_logger
from celery import group, chord, chain
from celery import shared_task#, task
from django.shortcuts import get_object_or_404
from django.http import Http404
# Channel layer imports & assignment
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()
# local imports
from .helpers import get_num_currencies, get_coin_data
from .models import Coin
from .serializers import CoinSerializer
from celery.result import allow_join_result
from celery.five import monotonic
from celery.utils.log import get_task_logger
from contextlib import contextmanager
from django.core.cache import cache
from hashlib import md5
from celery.utils.log import get_task_logger
# import multiprocessing
DELTA = timedelta(minutes=5)
DELTA1 = timedelta(minutes=1)
DELTA2 = timedelta(minutes=2)
DELTA3 = timedelta(minutes=3)
DELTA4 = timedelta(minutes=4)
TIMEOUT = 60
# TIME_OFFSET = datetime.utcnow() - datetime.now()
"""
workflow:
Chain these actions to gether

1. Get the total number of currencies e.i. 16xx
2. Divde the worload in in groups of 100 different coins
3. Send request to coinmarketcap API in parallel
4. Update database 
5. Schedule next task
"""
logger = get_task_logger(__name__)

# Task locking mechanism to limit duplicate tasks
def memcache_lock(lock_id, task_name):
    # cache.add fails if the key already exists
    status = cache.add(lock_id, task_name, TIMEOUT) 
    return status

# Get number of currencies to calculate how many 
# pages of data we need to fetch
@shared_task
def get_task_count():
    count = get_num_currencies()
    if count != 0:
        return count
    print('Get task returned zero task. Do you have internet connection?')

# Fetch coins from API pages in chunks of 100 (default)
@shared_task
def fetch_data(start=0, num_coins=100):
    if num_coins > 100:
        print("You can only request maximum of 100 coins per API call")
        raise EOFError
    data = get_coin_data(start=start, limit = num_coins)
    return data #(data[key] for key in data.keys()

@shared_task
def divide_data(coin_dict):
    iterator = (key for key in coin_dict.keys())
    return [coin_dict[key] for key in iterator]

@shared_task
def update_or_create_obj(coin_list):
    # if data save valid then call channel group HERE
    for coin in coin_list:
        id = coin['id']
        # ID = coin['name']
        defaults = coin
        obj, created = Coin.objects.update_or_create(id=id, defaults=defaults)
        # await channel_layer.group_send(
        #     coin_name,
        #     coin
        # )
        # if the above fails, try this;
        async_to_sync(channel_layer.group_send)(
            'table', 
            {
                "type": "receive_json",
                "content": json.dumps(coin),
            }
        )
        if created:
            print("New coin %s created" %obj.name)


@shared_task
def last_update_stamp():
    coins = Coin.objects.all().order_by('-last_updated')
    for coin in coins:
        if coin.last_updated != None:
            return coin.last_updated        

    raise Http404('No valid timestamp has turned up')  

def pipe():
    try:
        coin_count = get_num_currencies() 
        iter_pages = (100*i for i in range(ceil(coin_count/100)))
        # run multiple assembly lines in parallel (approx 17)
        assembly_lines = group(
            [
                chain(
                    fetch_data.s(i),
                    divide_data.s(),
                    update_or_create_obj.s(),
                    ) for i in iter_pages
            ]
        )
        assembly_lines().get()
        # timestamp = Coin.objects.all()[10].last_updated
        timestamp =  (assembly_lines | 
                        last_update_stamp.si()
                        )().get()
        return timestamp
    
    except Exception as e:
        print(e)
    
def run_pipe():
    timestamp = pipe()
    while True:    
        Bitcoin = Coin.objects.get(id=1)
        reference_t = Bitcoin.last_updated
        countdown = ceil(reference_t - time.time()) + 300 + 1
        
        while countdown < 0:
            print('Received negative countdown. \
                Recalibrating...')
            time.sleep(5)
            new_time = recalibrate_time(coin_id=1)
            countdown = ceil(new_time - time.time()) + 300 + 1
                        
        print('Waiting %d seconds' %countdown)
        time.sleep(countdown)
        pipe()

def recalibrate_time(coin_id):
    coin = get_coin_data(coin_id, limit=1)[str(coin_id)]
    return coin['last_updated']

@shared_task
def recurse_pipe():
    # TODO: refactor this to update once every night as a background task
    
    # We use a mem-cache lock to avoid duplicate pipes.
    # lock_string = str(Coin.objects.get(id=1).last_updated)
    # lock_utf8 = lock_string.encode('utf-8')
    # lock_id = md5(lock_utf8).hexdigest()

    # if not memcache_lock(lock_id, 'recurse-pipe'):
    #     print('Exiting recurse_pipe', lock_string)
    # else:
    try:
        with allow_join_result():
            timestamp_last = pipe()            
            reference_timestamp = datetime.fromtimestamp(timestamp_last)
            eta = reference_timestamp + DELTA1
            # recurse_pipe.apply_async(eta=eta)
            if eta < datetime.now():
                # recurse_pipe.si().apply_async()
                recurse_pipe.apply_async(countdown=60)
            else:
                recurse_pipe.apply_async(eta=eta)
    
    except Exception as e:
        print(e)




# def recurse_pipe(eta=-1):
#     if eta == -1:
#         unix_time_stamp = pipe.delay().get()
#     else:
#         unix_time_stamp = pipe.apply_async(eta=eta).get()
    
#     print(unix_time_stamp)
#     last_updated = datetime.fromtimestamp(unix_time_stamp)
#     delta = timedelta(minutes=5)
#     eta = last_updated + delta
#     for i in range(100):
#         print('ETA:', eta)
#     # if for some reason next scheduled iteration is already past, call pipe NOW
#     if eta <= datetime.utcnow():
#         pipe.delay().get()

# recurse_pipe(eta=eta)
# Can only request 100 coins per API request
# fetch_jobs = group(renew_database.s(start) for start in starting_points))()
# callback = last_update_stamp.si()

# The callback will only be applied if the task exited successfully, 
# and it will be applied with the return value of the parent task as argument.
# result = chain(fetch_jobs, callback)()
# prev_update = result.get()
# create a controller or something. 
# BUt first, just test this pipe asynchronously and see how many workers it spawns
# Also, implement a way to control how many times coinmarketcap API gets called

# @shared_task
# def renew_database(start, num_coins=100):
#     print(datetime.now())
#     if num_coins > 100:
#         print("You can only request maximum of 100 coins per API call")
#         raise EOFError
#     response = get_coin_data(start=start, limit = num_coins)
#     for key in response.keys():
#         serializer = CoinSerializer(data=response[key])
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             # return JsonResponse(serializer.errors, status=400)
#             print('Invalid serialization')
#             continue



# import asyncio
# import datetime

# async def display_date(loop):
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)

# loop = asyncio.get_event_loop()
# # Blocking call which returns when the display_date() coroutine is done
# loop.run_until_complete(display_date(loop))
# loop.close()




# renew_database.apply_async(countdown=5)

# df = get_listings()
# # just wipe the whole coin database
# coin_objects = Coin.objects.all()#.filter(API_ID = coin['API_ID'])
# coin_objects.delete()

# for index in df.index:
#     coin = df.loc[index].to_dict()
#     serializer = CoinSerializer(data=coin)
#     if serializer.is_valid():
#         serializer.save()
#         # print(" %s has been updated" % serializer.data['name'])

# last_updated = datetime.fromtimestamp(df['last_updated'][0])
# delta = timedelta(minutes=5)
# print(datetime.now())
# eta = last_updated + delta
# # countdown = last_updated + delta - datetime.now()
# # print(countdown)
# # time.wait(10)# 10 seconds wait
# renew_database.apply_async(eta=eta)#eta=eta

# renew_database()

# app.control.purge()
