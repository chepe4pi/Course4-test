from rest_framework import serializers

from service.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    plan = PlanSerializer()
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        return (instance.plan.discount_percent / 100) * instance.service.full_price

    class Meta:
        model = Subscription
        fields = ('id', 'start_date', 'end_date', 'client_name', 'email', 'plan', 'price')
