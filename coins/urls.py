# Stdlib imports
from __future__ import absolute_import
# Core Django imports
from django.conf.urls import url, include
from django.views.generic import RedirectView
# Third-party app imports
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
# Imports from your apps
from . import views
from .views import CoinViewSet

router = routers.DefaultRouter()
router.register(r'coins', CoinViewSet)
# redirect api root to github readme.md page
redirect_url = 'https://github.com/j24ohuw/coinmarketcap-websocket-extension/blob/master/README.md'

urlpatterns = [
    url(r'^api/$', RedirectView.as_view(url=redirect_url)),
    url(r'^api/', include(router.urls)),
    # url(r'^table/$', views.tableView),
    # url(r'^chat/$', views.index, name='index'),
    # url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'^([A-Za-z-]+)/$', views.coin_detail),
    url(r'^api/hist/(?P<symbol>[\w]+)/$', views.historical_data_view),
    url(r'^api/search', views.CoinSearchListView.as_view()),
]


# urlpatterns = format_suffix_patterns(urlpatterns)
# chat/urls.py

