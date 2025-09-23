from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_details, name='web'),
    path('about/', views.web_details, name='about')
]