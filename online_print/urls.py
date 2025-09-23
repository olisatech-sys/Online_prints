
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('design_and_print.urls')),
    path('website/', include('web_dev.urls')),
]
