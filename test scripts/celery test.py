from celery import Celery
from datetime import timedelta, datetime
app = Celery('tasks', broker='redis://guest@localhost//')

@app.task
def print_time():
    print(datetime.datetime.now())
    delta = timedelta(minutes=5)
    print_time.apply_sync(countdown=3)
