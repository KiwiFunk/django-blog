from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class HomeView(ListView):                       # ListView is used to display a list of objects.
    model = Post                                # The model that this view will use to query the database.
    template_name = 'home.html'                 # The template that this view will use to generate the HTML.

class PostDetailView(DetailView):               # DetailView is used to display a single object in detail.
    model = Post
    template_name = 'post_details.html'         # The template that this view will use to generate the HTML.