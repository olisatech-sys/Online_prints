from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    phone= models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pic', null=True, blank=True)


class Service(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    date_published = models.DateField()

    def __str__(self):
        return f'{self.name} by {self.author}'
    
class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    sample_image = models.ImageField(upload_to='sample_image', null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service} made by {self.client}'
