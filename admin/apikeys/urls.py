from django.urls import path
from .views import APIKeysListView

urlpatterns = [
    path('apikeys/', APIKeysListView.as_view(), name='apikeys'),
]
