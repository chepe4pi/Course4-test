from rest_framework import serializers

from service.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')

    class Meta:
        model = Subscription
        fields = ('id', 'start_date', 'end_date', 'client_name', 'email')
