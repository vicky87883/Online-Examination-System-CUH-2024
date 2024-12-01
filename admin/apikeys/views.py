from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import APIKeys
from .serializers import APIKeysSerializer

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
