from celery import Celery
from datetime import timedelta, datetime
import os
import time
os.environ['FORKED_BY_MULTIPROCESSING']= "1"
app = Celery('tasks', broker='redis://localhost//')

@app.task
def print_time():
    print(datetime.now())
    print_time.apply_async(countdown=10)
    
