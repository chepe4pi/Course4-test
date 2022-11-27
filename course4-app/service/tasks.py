import time

from celery import shared_task
from celery_singleton import Singleton

from service.models import Subscription


@shared_task(base=Singleton)
def set_price(subscription_id):
    time.sleep(30)
    subscription = Subscription.objects.get(id=subscription_id)
    new_price = subscription.service.full_price - subscription.service.full_price * (subscription.plan.discount_percent / 100)
    subscription.price = new_price
    subscription.save()
