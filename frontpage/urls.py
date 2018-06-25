from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    url(r'^frontpage', views.coin_list, name='coin_list'),
    url(r'^template/$', views.template),
    url(r'^paginator/$', views.coin_list_interactive)
]