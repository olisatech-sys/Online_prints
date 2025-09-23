from django.shortcuts import render
from .models import Service, Book


# Create your views here.
def home(request):
    services = Service.objects.all()
    books = Book.objects.all()
    context = {
        "services": services,
        "books": books
    }
    return render(request, 'index.html', context)