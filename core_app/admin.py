from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish_date', 'quantity', 'date_uploaded')
admin.site.register(Book, BookAdmin)
# admin.site.register(Book)
# admin.site.register(Purchase)