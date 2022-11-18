from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100)
    country = CountryField()
    full_address = models.CharField(max_length=100)
