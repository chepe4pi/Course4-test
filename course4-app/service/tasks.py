import datetime
import time

from celery import shared_task
from celery_singleton import Singleton
from django.db import transaction

from service.models import Subscription


@shared_task(base=Singleton)
def set_price(subscription_id):
    with transaction.atomic():
        time.sleep(5)
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)
        time.sleep(30)
        new_price = subscription.service.full_price - subscription.service.full_price * (subscription.plan.discount_percent / 100)
        subscription.price = new_price
        subscription.save()
    print('everything else')


@shared_task(base=Singleton)
def other_task(subscription_id):
    with transaction.atomic():
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)
        time.sleep(45)
        subscription.comment = str(datetime.datetime.now())
        subscription.save()
    print('everything else')
