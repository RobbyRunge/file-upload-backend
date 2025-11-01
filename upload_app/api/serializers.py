from rest_framework import serializers
from upload_app.models import FileUpload


# Für die Serialisierung des FileUpload-Modells
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        # Das zu serialisierende Modell
        model = FileUpload
        # Die zu serialisierenden Felder
        fields = ['file', 'uploaded_at']