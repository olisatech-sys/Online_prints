from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish_date', 'quantity', 'date_uploaded')
    list_filter = ('title', 'publish_date')
    search_fields = ('title',)
admin.site.register(Book, BookAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'price', 'purcharsed_by', 'date_purchased')
admin.site.register(Purchase, PurchaseAdmin)