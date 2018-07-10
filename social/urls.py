from django.urls import include, path
from django.conf.urls import url
from .views import home
from django.contrib.auth import views
from . import views as coreview
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')), 
    url(r'^signup/$', coreview.signup, name='logout'),
    # url(r'^loginpage/loginhome/$', home, name='home'),
]
