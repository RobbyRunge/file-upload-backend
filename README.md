# File-Upload Backend (Django REST Framework)

A Django-based backend project for uploading and managing files via a REST API.

## � Frontend Repository

The corresponding frontend application for this backend can be found here:  
**[https://github.com/RobbyRunge/file-upload-frontend](https://github.com/RobbyRunge/file-upload-frontend)**

---

## �📋 Table of Contents

- [About the Project](#about-the-project)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Data Models](#data-models)
- [Admin Panel](#admin-panel)
- [Troubleshooting](#troubleshooting)

---

## 🎯 About the Project

This project is a backend system for file uploads, developed with Django and Django REST Framework. It enables:

- **File Upload** via REST API
- **Automatic Storage** of files in the `media/uploads/` directory
- **Timestamp Tracking** for each upload
- **RESTful API** for integration with frontend applications
- **Admin Interface** for managing uploaded files
- **CORS Support** for frontend integration

The frontend application for this backend is available at:  
[https://github.com/RobbyRunge/file-upload-frontend](https://github.com/RobbyRunge/file-upload-frontend)

---

## 🛠 Technology Stack

- **Python** 3.x
- **Django** 5.2.7
- **Django REST Framework** 3.16.1
- **SQLite** (Database)
- **ASGI** 3.10.0

---

## 📁 Project Structure

```
modul-9.1-file-upload-backend/
│
├── img_upload/                 # Main project directory
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
│
├── upload_app/                 # Django app for file upload
│   ├── __init__.py
│   ├── admin.py               # Admin configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Data models
│   ├── views.py               # Views
│   ├── tests.py               # Tests
│   │
│   ├── api/                   # REST API
│   │   ├── serializers.py     # DRF Serializers
│   │   ├── views.py           # API Views
│   │   └── urls.py            # API URLs
│   │
│   └── migrations/            # Database migrations
│       ├── __init__.py
│       └── 0001_initial.py
│
├── media/                      # Uploaded files (created automatically)
│   └── uploads/               # Upload directory
│
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python Package Manager)
- Virtual environment (recommended)

### Step-by-Step Guide

#### 1. Clone or download the repository

```bash
git clone <repository-url>
cd modul-9.1-file-upload-backend
```

#### 2. Create a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` contains:
- Django==5.2.7
- djangorestframework==3.16.1
- asgiref==3.10.0
- sqlparse==0.5.3
- tzdata==2025.2

#### 4. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

**Important:** This step creates all necessary database tables, including `auth_user` for user management.

#### 5. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts and enter:
- Username
- Email address (optional)
- Password (twice for confirmation)

#### 6. Start the development server

```bash
python manage.py runserver
```

The server is now running at: `http://127.0.0.1:8000/`

---

## ⚙️ Configuration

### Media Files Settings

In `img_upload/settings.py`:

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Media files settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- **MEDIA_ROOT**: Absolute path to the directory for uploaded files
- **MEDIA_URL**: URL prefix for accessing media files

### URL Configuration

In `img_upload/urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('upload_app.api.urls')),
]

# Serving media files in development mode
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Note:** The `static()` function should only be used in development mode. For production, use a web server like Nginx or Apache.

---

## 📖 Usage

### Upload a file (POST Request)

**Endpoint:** `POST http://127.0.0.1:8000/api/upload/`

**With cURL:**
```bash
curl -X POST http://127.0.0.1:8000/api/upload/ \
  -F "file=@/path/to/file.jpg"
```

**With Python (requests):**
```python
import requests

url = 'http://127.0.0.1:8000/api/upload/'
files = {'file': open('file.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.json())
```

**With JavaScript (Fetch API):**
```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('http://127.0.0.1:8000/api/upload/', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

**Note:** For a complete frontend implementation example check out the frontend repository:  
[https://github.com/RobbyRunge/file-upload-frontend](https://github.com/RobbyRunge/file-upload-frontend)

**Successful Response (201 CREATED):**
```json
{
    "file": "/media/uploads/file.jpg",
    "uploaded_at": "2025-11-01T12:34:56.789Z"
}
```

**Error Response (400 BAD REQUEST):**
```json
{
    "file": ["This field is required."]
}
```

---

## 🔌 API Endpoints

### 1. Upload File

- **URL:** `/api/upload/`
- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Authentication:** None (can be added if needed)

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| file | File | Yes | The file to upload |

**Response:**

| Field | Type | Description |
|-------|------|-------------|
| file | String | Relative path to the uploaded file |
| uploaded_at | DateTime | Upload timestamp (ISO 8601) |

### 2. Admin Interface

- **URL:** `/admin/`
- **Method:** `GET`
- **Authentication:** Superuser login required

---

## 💾 Data Models

### FileUpload Model

Defined in `upload_app/models.py`:

```python
from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
```

**Fields:**

- **file** (`FileField`): 
  - Stores the uploaded file
  - Upload path: `media/uploads/`
  - Supports all file types

- **uploaded_at** (`DateTimeField`):
  - Automatically set timestamp
  - Set when the object is created (`auto_now_add=True`)
  - Format: ISO 8601 (e.g., "2025-11-01T12:34:56.789Z")

### FileUploadSerializer

Defined in `upload_app/api/serializers.py`:

```python
from rest_framework import serializers
from upload_app.models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['file', 'uploaded_at']
```

- Converts model data to JSON and vice versa
- Automatically validates incoming data
- Serializes both fields (`file` and `uploaded_at`)

---

## 👨‍💼 Admin Panel

### Accessing the Admin Panel

1. Make sure the server is running:
   ```bash
   python manage.py runserver
   ```

2. Open in your browser: `http://127.0.0.1:8000/admin/`

3. Log in with your superuser credentials

### Features in the Admin Panel

- **View files**: List of all uploaded files
- **Delete files**: Remove uploads
- **File information**: Display upload timestamp and file path
- **User management**: Create and manage users
- **Permissions**: Assign admin rights

### Register FileUpload in Admin

In `upload_app/admin.py`:

```python
from django.contrib import admin
from .models import FileUpload

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['file']
    readonly_fields = ['uploaded_at']
```

---

## 🔧 Troubleshooting

### Problem: "no such table: auth_user"

**Cause:** Database tables were not created.

**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Problem: Files are not being uploaded

**Possible causes:**

1. **MEDIA_ROOT not configured**
   - Check `settings.py`
   - Make sure `MEDIA_ROOT` and `MEDIA_URL` are set

2. **Missing write permissions**
   - Check file permissions for the `media/` directory
   - Windows: Right-click → Properties → Security
   - Linux/macOS: `chmod 755 media/`

3. **Incorrect Content-Type**
   - Use `multipart/form-data` for POST requests
   - Make sure the field is named "file"

### Problem: 404 Error for media files

**Cause:** Media URLs not configured correctly.

**Solution:** Make sure the following is in `img_upload/urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Note:** This only works in debug mode (`DEBUG = True`).

### Problem: CSRF Token missing

**Cause:** CSRF protection is enabled.

**Solutions:**

1. **For API usage:** Disable CSRF protection for API views:
   ```python
   from django.views.decorators.csrf import csrf_exempt
   from django.utils.decorators import method_decorator
   
   @method_decorator(csrf_exempt, name='dispatch')
   class FileUploadView(APIView):
       # ...
   ```

2. **For frontend integration:** Send CSRF token in request:
   ```javascript
   fetch('/api/upload/', {
       method: 'POST',
       headers: {
           'X-CSRFToken': getCookie('csrftoken')
       },
       body: formData
   });
   ```

### Problem: Module not found

**Error:** `ModuleNotFoundError: No module named 'rest_framework'`

**Solution:**
```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate       # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

---

## 🔒 Security Notes

### For Development

- `DEBUG = True` is fine for development
- `SECRET_KEY` should remain secret
- SQLite is sufficient for development and testing

### For Production

1. **Disable DEBUG:**
   ```python
   DEBUG = False
   ```

2. **Change SECRET_KEY:**
   ```python
   SECRET_KEY = 'your-secure-production-key'
   ```

3. **Set ALLOWED_HOSTS:**
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Use production database:**
   - PostgreSQL (recommended)
   - MySQL/MariaDB
   - Not SQLite!

5. **Serve media files via web server:**
   - Nginx or Apache
   - Not via Django!

6. **Set file size limits:**
   ```python
   # settings.py
   DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB
   FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB
   ```

7. **Add file type validation:**
   ```python
   # serializers.py
   class FileUploadSerializer(serializers.ModelSerializer):
       def validate_file(self, value):
           allowed_types = ['image/jpeg', 'image/png', 'application/pdf']
           if value.content_type not in allowed_types:
               raise serializers.ValidationError('File type not allowed')
           return value
   ```

8. **Add authentication:**
   ```python
   # views.py
   from rest_framework.permissions import IsAuthenticated
   
   class FileUploadView(APIView):
       permission_classes = [IsAuthenticated]
   ```

---

## 📚 Further Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django File Uploads](https://docs.djangoproject.com/en/stable/topics/http/file-uploads/)
- [Django Media Files](https://docs.djangoproject.com/en/stable/howto/static-files/)
- [Frontend Repository](https://github.com/RobbyRunge/file-upload-frontend)

---

## 📝 License

This project was created for educational purposes (Developer Academy - Module 9.1).

---

## 👤 Contact

For questions or issues, please contact the project manager.

---

**Good luck with your File-Upload Backend! 🚀**
