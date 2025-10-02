from django.shortcuts import render
from .models import Book
# Create your views here.
def home(request):
    books = Book.objects.all().order_by('-date_uploaded')
    context = {
        'books': books,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def books_view(request):
    books = Book.objects.all().order_by('-date_uploaded')
    context = {
        'books': books,
    }
    return render(request, 'books.html', context)