from django.contrib import admin

from contact.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','last_name', 'email', 'subject', 'message', 'updated_date', 'created_date']
    search_fields = ['name', 'last_name', 'email', 'subject', 'message']


    class Meta:
        model = Message
    
# Register your models here.

