from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from subscribers.models import Subscriber
from subscribers.serializers import SubscriberSerializers, SubscriberPostSerializers


class Subscribers(APIView):

    def get(self, request):
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializers(subscribers, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        subscriber = SubscriberPostSerializers(data=request.data)
        if subscriber.is_valid():
            subscriber.save()
            return Response({'status': "Add"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
