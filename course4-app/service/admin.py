from django.contrib import admin

from service.models import Service, Plan, Subscription

admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscription)
