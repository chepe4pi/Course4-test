from django.contrib.auth.models import User
from django.db.models import Prefetch, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from service.models import Subscription
from service.serializers import SubscriptionSerializer


class SubscriptionsView(ReadOnlyModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch('client', queryset=Client.objects.all().select_related('user').only(
            'company_name',
            'user__email')),
    )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comment', 'price']
