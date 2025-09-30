from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    publish_date = models.DateField()
    quantity = models.IntegerField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


# purchase
class Purchase(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    purcharsed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book_name} purchased by {self.purcharsed_by}'