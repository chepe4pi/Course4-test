from django.contrib.auth.models import User
from django.db.models import Prefetch, F
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from service.models import Subscription
from service.serializers import SubscriptionSerializer


class SubscriptionsView(ReadOnlyModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all().prefetch_related(
        # 'plan',
        # 'service',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only(
            'company_name',
            'user__email')),

    )#.annotate(a_price=F('plan__discount_percent') * F('service__full_price') / 100.00
    #)
