from django.core.validators import MaxValueValidator
from django.db import models
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveSmallIntegerField()

    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.__original_full_price = self.full_price

    def save(self, *args, **kwargs):
        from .tasks import set_price, other_task

        super().save(*args, **kwargs)

        if self.__original_full_price != self.full_price:
            for subscription in self.subscription_set.all():
                set_price.delay(subscription.id)
                other_task.delay(subscription.id)


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )
    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveSmallIntegerField(default=0,
                                                        validators=[
                                                            MaxValueValidator(100),
                                                        ])

    def __init__(self, *args, **kwargs):
        super(Plan, self).__init__(*args, **kwargs)
        self.__original_discount_percent = self.discount_percent

    def save(self, *args, **kwargs):
        from .tasks import set_price, other_task

        super().save(*args, **kwargs)

        if self.__original_discount_percent != self.discount_percent:
            for subscription in self.subscription_set.all():
                set_price.delay(subscription.id)
                other_task.delay(subscription.id)


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True)
    comment = models.CharField(max_length=50, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    start_date = models.DateField() # ??
    end_date = models.DateField() # ??
    price = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    class Meta:
        indexes = [
            models.Index(fields=['comment', 'price']),
        ]
