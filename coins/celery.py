from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# Windows workaround. Remove for Linux environment
# os.environ['FORKED_BY_MULTIPROCESSING']= "1"
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

app = Celery('coins')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.broker_transport_options = {'visibility_timeout': 43200}



