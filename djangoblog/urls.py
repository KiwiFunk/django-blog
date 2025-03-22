from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('users/', include('django.contrib.auth.urls')),            # Using Django Authentication System.
    path('users/', include('usersystem.urls')),                     # Our usersystem app.
]
