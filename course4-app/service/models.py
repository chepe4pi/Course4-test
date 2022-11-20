from django.core.validators import MaxValueValidator
from django.db import models
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveSmallIntegerField()


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


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
