from django.db import models

# Modell für den Datei-Upload (es wird ein 'media/' Ordner erstellt mit einem 'uploads/' Unterordner)
class FileUpload(models.Model):
    # Das hochgeladene Datei-Feld (speichert die Datei im 'uploads/' Verzeichnis)
    file = models.FileField(upload_to='uploads/')
    # Das Datum und die Uhrzeit des Uploads (automatisch beim Erstellen gesetzt)
    uploaded_at = models.DateTimeField(auto_now_add=True)