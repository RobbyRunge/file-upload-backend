from django.urls import path
from .views import FileUploadView

urlpatterns = [
    # URL-Pfad für den Datei-Upload
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]