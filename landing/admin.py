from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name_user' , 'email_user']
    #list_display=[field.name for field in Subscriber.name_user]
    #exclude = ['email_user']
    list_filter=['name_user']
    search_fields = ['name_user','email_user']

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)