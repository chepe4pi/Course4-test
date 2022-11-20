from rest_framework import serializers

from service.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    a_price = serializers.CharField()

    class Meta:
        model = Subscription
        fields = ('id', 'start_date', 'end_date', 'client_name', 'email',
                  'a_price')
