import time

from django.conf import settings
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course4app.settings')
app = Celery('course4app')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    time.sleep(60)
    print(f'Request: {self.request!r}')