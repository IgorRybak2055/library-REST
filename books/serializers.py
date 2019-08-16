from rest_framework import serializers
from books.models import Book


class BookSerializers(serializers.ModelSerializer):
    '''Сериализация книг'''

    class Meta:
        model = Book
        fields = ('id', 'author', 'genre', 'book_name', 'language')


class BookPostSerializers(serializers.ModelSerializer):
    '''Сериализация книг'''

    class Meta:
        model = Book
        fields = ('author', 'genre', 'book_name', 'language')

