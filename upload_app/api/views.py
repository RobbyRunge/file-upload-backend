from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from upload_app.models import FileUpload
from .serializers import FileUploadSerializer

# Ansicht für den Datei-Upload
class FileUploadView(APIView):
    # POST-Methode zum Hochladen von Dateien
    def post(self, request, format=None):
        # Validierung und Speicherung der hochgeladenen Datei
        serializer = FileUploadSerializer(data=request.data)
        # Überprüfung, ob die Daten gültig sind
        if serializer.is_valid():
            # Speichern der Datei
            serializer.save()
            # Rückgabe der erfolgreichen Antwort
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Rückgabe der Fehlerantwort bei ungültigen Daten
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)