from django.contrib import admin

from upload_app.models import FileUpload

# Registrierung des FileUpload-Modells im Admin-Interface
admin.site.register(FileUpload)