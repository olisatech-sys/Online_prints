from django.shortcuts import render

# Create your views here.
def web_details(request):
    return render(request, 'web-details.html')