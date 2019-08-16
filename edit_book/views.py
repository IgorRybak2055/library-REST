from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializers, BookPostSerializers


class EditBook(APIView):
    def get(self, request, id):
        try:
            book_info = BookSerializers(Book.objects.filter(id=id),many=True)
            return Response({'book_info': book_info.data})
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            serializer = BookPostSerializers(Book.objects.defer('id').get(id=id), request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Save'})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
