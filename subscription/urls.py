# Core Django imports
from django.conf.urls import url, include
# Imports from your apps
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'subscription', views.SubscriptionViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]