from django.contrib import admin
from .models import Message, Rules, ContentIndex

admin.site.register(Message)
admin.site.register(Rules)
admin.site.register(ContentIndex)
