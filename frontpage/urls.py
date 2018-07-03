from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    url(r'^$', views.coin_list, name='home'),
    url(r'^template/$', views.templateView),
]
