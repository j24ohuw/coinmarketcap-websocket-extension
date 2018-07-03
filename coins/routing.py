# chat/routing.py
from django.conf.urls import url
# mysite/routing.py

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/table/$', consumers.CoinConsumer),
    url(r'^ws/coin/(?P<coin_slug>[^/]+)/$', consumers.CoinDetailConsumer),
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]


