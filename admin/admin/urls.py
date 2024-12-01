# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('examapi.urls')),  # Include app URLs
    path('api/', include('apikeys.urls')),
]
