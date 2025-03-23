from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
class UserRegistrationView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')                 # Redirect to login after successful registration.

class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')                  # Redirect to home after updating the profile.