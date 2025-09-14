from django.contrib import admin

from .models import Message, Group, Event

admin.site.register(Message)
admin.site.register(Event)
admin.site.register(Group)
