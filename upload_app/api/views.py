from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from upload_app.models import FileUpload
from .serializers import FileUploadSerializer

class FileUploadView(APIView):
    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)