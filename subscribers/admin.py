from django.contrib import admin
from subscribers.models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Subscriber, SubscriberAdmin)
