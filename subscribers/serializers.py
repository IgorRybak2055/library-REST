from rest_framework import serializers
from subscribers.models import *


class SubscriberSerializers(serializers.ModelSerializer):
    '''Сериализация подписчиков'''

    class Meta:
        model = Subscriber
        fields = ('id', 'first_name', 'last_name', 'address', 'phone')


class SubscriberPostSerializers(serializers.ModelSerializer):
    '''Сериализация подписчиков'''

    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'address', 'phone')


# class SubscriptionsSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Subscriptions
#         fields = ('user_id', 'book_id')