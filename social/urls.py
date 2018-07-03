from django.urls import include, path
from django.conf.urls import url
from .views import home
from django.contrib.auth import views
    
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')), 
    #url(r'^loginpage/loginhome/$', home, name='home'),
]
