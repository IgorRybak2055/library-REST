from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import Book, Subscriptions
from subscribers.models import Subscriber
from subscribers.serializers import SubscriberSerializers
from books.serializers import BookSerializers, BookPostSerializers


class Books(APIView):
    def get(self, request, id):
        books = BookSerializers(Book.objects.filter(subscriptions__user_id=id), many=True)
        free_books = BookSerializers(Book.objects.filter(free=True), many=True)
        return Response({'users_books': books.data, 'free_books': free_books.data})

    def put(self, request, id):
        book = Book.objects.get(id=id)
        book.free = True
        book.save()
        Subscriptions.objects.get(book_id=book).delete()
        return Response({'status': 'Free'})

    def post(self, request, id):
        book = Book.objects.get(book_name=request.data['book_name'])
        subscription = Subscriptions(user_id=Subscriber.objects.get(id=id),
                                     book_id=book)

        book.free = False
        subscription.save()
        book.save()
        return Response({'status': 'Add'})


class FreeBooks(APIView):
    def get(self, request):
        free_books = BookSerializers(Book.objects.filter(free=True), many=True)
        return Response({'free_books': free_books.data})

    def post(self, request):
        book = BookSerializers(data=request.data)

        if book.is_valid():
            book.save()
            return Response({'status': 'Add'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)