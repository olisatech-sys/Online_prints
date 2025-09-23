from django.contrib import admin
from .models import Service, Book, Profile, Booking
# Register your models here.

admin.site.register(Service)
admin.site.register(Book)
admin.site.register(Booking)
admin.site.register(Profile)