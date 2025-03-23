from django.urls import path
from .views import UserRegistrationView, EditProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
]