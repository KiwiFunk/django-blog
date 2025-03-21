from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm

# Create your views here.

class HomeView(ListView):                       # ListView is used to display a list of objects.
    model = Post                                # The model that this view will use to query the database.
    template_name = 'home.html'                 # The template that this view will use to generate the HTML.

class PostDetailView(DetailView):               # DetailView is used to display a single object in detail.
    model = Post
    template_name = 'post_details.html'         # The template that this view will use to generate the HTML.

class CreatePostView(CreateView):               # CreateView is used to create a new post object.
    model = Post
    form_class = PostForm                       # The form that this view will use to generate the form fields.
    template_name = 'create_post.html'          # The template that this view will use to generate the HTML.
    # Fields are now defined in forms.py
     
class UpdatePostView(UpdateView):               # UpdateView is used to update an existing post object.
    model = Post
    template_name = 'update_post.html'          # The template that this view will use to generate the HTML.
    fields = ['title', 'title_tag', 'summary', 'body']