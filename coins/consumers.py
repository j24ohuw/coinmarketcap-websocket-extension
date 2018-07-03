# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from channels.exceptions import InvalidChannelLayerError
import json


"""
We establish each coin as a channel and feed data to each member connected the channel (Group)

TODO:
1. Each coin as a channel on its own and update the entire HTML page 
2. Chunk coins in groups of 40 and update only the coins currently shown in the page
"""
class CoinConsumer(AsyncJsonWebsocketConsumer):
    groups = ["broadcast"]

    async def connect(self):
    # User/Client is added to individual coin group given by coin_name as follows: 
        try:
            await self.channel_layer.group_add(
                "table",
                self.channel_name
            )
            await self.accept()
        
        except ValueError:
            log.debug('invalid channel name %s', self.channel_name)
            return
        except InvalidChannelLayerError:
            log.debug('Invalid channel name %s or channel does not exist yet', self.channel_name)
            return

    # Receives coin_data dict and pass it to the user
    async def receive_json(self, content):
        try:
            await self.send_json(content)  
        except:
            return
    
    async def coin_message(self, event):
        print(event['coin_update'])
        self.send_json(content=event['coin_update'])

    async def disconnect(self, close_code):
        #leave room group
        await self.channel_layer.group_discard(
            "table",
            self.channel_name
        )



# individual coin channel consumer for subscription model
# logged in users get periodic updates whenever coin data they subscribe to get updated
class CoinDetailConsumer(AsyncJsonWebsocketConsumer):
    groups = ["broadcast"]

    async def connect(self):
        self.coin_slug = self.scope['url_route']['kwargs']['coin_slug']
    # User/Client is added to individual coin group given by coin_name as follows: 
        try:
            await self.channel_layer.group_add(
                self.coin_slug,
                self.channel_name
            )
            await self.accept()
        
        except ValueError:
            log.debug('invalid coin name %s', coin_slug)
            return
        except InvalidChannelLayerError:
            log.debug('Invalid channel name %s or channel does not exist yet', self.channel_name)
            return

    # Receives coin_data dict and pass it to the user
    async def receive_json(self, content):
        try:
            await self.send_json(content)  
        except:
            return Response()
    
    # async def alert(self, event):
    #     print(event['coin_update'])
    #     self.send_json(content=event['coin_update'])

    async def disconnect(self, close_code):
        #leave room group
        await self.channel_layer.group_discard(
            self.coin_slug,
            self.channel_name
        )


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.coin_name = self.scope['url_route']['kwargs']['coin_name']

#         # Join room group
#         await self.channel_layer.group_add(
#             self.coin_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))





# await self.channel_layer.group_send(
#     self.coin_name,
#     { 
#     # special type key corresponding to the name of a follow-up task method should to be assigned 
#     'type': 'push_coin_data',
#     'rank': coin_data['rank'],
#     'name': coin_data['name'],
#     'price': coin_data['price'],
#     'volume': coin_data['volume'],
#     'marketcap':, coin_data['market_cap'],
#     'circulating_supply': coin_data['circulating_supply'],
#     'percent_change_24h': coin_data['percent_change_24h'],
#     }
# )

# if coin_data['name'] != self.coin_name:
#     log.debug('self.coin_name does not match the passed coin name %s', coin_data['name'])
#     return
# message = text_data_json['message']
# json.loads(coin_)
# print(coin_data)