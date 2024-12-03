from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import APIKeys
from .serializers import APIKeysSerializer
import requests
from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)
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
    api_url = "http://127.0.0.1:8000/api/apikeys/"
    try:
        response = requests.get(api_url)
        logger.info(f"API Response: {response.status_code}")
        if response.status_code == 200:
            api_data = response.json()
            logger.info(f"Fetched API Data: {api_data}")
        else:
            api_data = {"error": "Could not fetch data"}
    except Exception as e:
        logger.error(f"Error fetching API data: {e}")
        api_data = {"error": "Could not fetch data"}
    return render(request, 'assignment.html', {'api_data': api_data})
