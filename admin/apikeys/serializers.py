from rest_framework import serializers
from .models import APIKeys

class APIKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKeys
        fields = '__all__'
