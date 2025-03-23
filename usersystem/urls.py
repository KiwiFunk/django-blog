from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, UserProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile', UserProfilePageView.as_view(), name='user_profile'),
]
