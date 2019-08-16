from django.db import models

from subscribers.models import Subscriber


class Book(models.Model):
    '''Модель книги'''

    author = models.CharField(max_length= 30, null=False)
    genre = models.CharField(max_length=10)
    book_name = models.CharField(max_length=50, null=False)
    language = models.CharField(max_length=20)
    free = models.BooleanField(null=False, default=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Subscriptions(models.Model):
    user_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
