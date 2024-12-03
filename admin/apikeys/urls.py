from django.urls import path
from .views import APIKeysListView
from django.urls import path
from .views import apikeys_view
urlpatterns = [
    path('apikeys/', APIKeysListView.as_view(), name='apikeys'),
]
