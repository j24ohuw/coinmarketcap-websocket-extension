from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'api/users/$', views.UserCreate.as_view(), name='account-create'),
    url(r'api/userlist/$', views.UserList.as_view()),
    
]