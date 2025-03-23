from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('users/', include('django.contrib.auth.urls')),            # Using Django Authentication System.
    path('users/', include('usersystem.urls')),                     # Our usersystem app.
    path('summernote/', include('django_summernote.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)