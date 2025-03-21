from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class HomeView(ListView):
    model = Post                                # The model that this view will use to query the database.
    template_name = 'home.html'                 # The template that this view will use to generate the HTML.