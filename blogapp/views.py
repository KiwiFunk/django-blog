from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):                       # ListView is used to display a list of objects.
    model = Post                                # The model that this view will use to query the database.
    template_name = 'home.html'                 # The template that this view will use to generate the HTML.
    ordering = ['-created_at']                  # The order in which the posts will be displayed on the home page.

class PostDetailView(DetailView):               # DetailView is used to display a single object in detail.
    model = Post
    template_name = 'post_details.html'         # The template that this view will use to generate the HTML.

class CreatePostView(CreateView):               # CreateView is used to create a new post object.
    model = Post
    form_class = PostForm                       # The form that this view will use to generate the form fields.
    template_name = 'create_post.html'          # The template that this view will use to generate the HTML.
    # Fields are now defined in forms.py

    def form_valid(self, form):                     # This method is called when valid form data has been POSTed.
        form.instance.author = self.request.user    # Set the author of the post to the current user.
        return super().form_valid(form)             # Call the parent class(CreateView)'s form_valid() method and pass form data as arg.
     
class UpdatePostView(UpdateView):               # UpdateView is used to update an existing post object.
    model = Post
    form_class = EditForm                       # The form that this view will use to generate the form fields.
    template_name = 'update_post.html'          # The template that this view will use to generate the HTML.

class DeletePostView(DeleteView):               # DeleteView is used to delete an existing post object.
    model = Post
    template_name = 'delete_post.html'          # The template that this view will use to generate the HTML.
    success_url = reverse_lazy('home')          # Redirect to the home page after deleting the post.

def CategoryView(request, cat):
    category_posts = Post.objects.filter(category__iexact=cat.replace('-', ' ')).order_by('-created_at')
    return render(request, 'categories.html', {
        'cats': cat.replace('-', ' ').title(),
        'category_posts': category_posts
    })