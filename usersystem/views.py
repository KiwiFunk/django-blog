from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm

# Create your views here.
class UserRegistrationView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')                 # Redirect to login after successful registration.

