from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import APIKeys
from .serializers import APIKeysSerializer
import requests
from django.shortcuts import render
class APIKeysListView(APIView):
    # Get all records
    def get(self, request):
        keys = APIKeys.objects.all()
        serializer = APIKeysSerializer(keys, many=True)
        return Response(serializer.data)

    # Create a new record
    def post(self, request):
        serializer = APIKeysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def apikeys_view(request):
    # Replace this with your actual API call or data fetching logic
    api_response = requests.get("http://127.0.0.1:8000/api/apikeys/")
    api_data = api_response.json()  # or whatever format the API returns

    return render(request, 'assignment.html', {'api_data': api_data})