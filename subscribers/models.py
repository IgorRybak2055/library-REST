from django.db import models


class Subscriber(models.Model):
    '''Модель пользователя библиотеки'''
    # id
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=15, null=False)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'


# class Subscriptions(models.Model):
#     user_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
#     book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)






