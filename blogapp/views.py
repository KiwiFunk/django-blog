from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse

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

def PostLikeView(request, pk):
    post = get_object_or_404(Post, id=pk)       # Get the post object with the given id. (404 if not found)
    if request.user in post.likes.all():
        post.likes.remove(request.user)         # Unlike if already liked
    else:
        post.likes.add(request.user)            # Like if not already liked
        if request.user in post.dislikes.all():
            post.dislikes.remove(request.user)  # Remove dislike if exists
    
    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))

def PostDislikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)      # Remove dislike
    else:
        post.dislikes.add(request.user)         # Add dislike
        if request.user in post.likes.all():
            post.likes.remove(request.user)     # Remove like if exists
    
    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))

def CommentLikeView(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        # Remove dislike if exists
        if request.user in comment.dislikes.all():
            comment.dislikes.remove(request.user)
    
    # Redirect back to the post detail page
    return HttpResponseRedirect(reverse('post_details', args=[str(comment.post.pk)]))

def CommentDislikeView(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.user in comment.dislikes.all():
        comment.dislikes.remove(request.user)
    else:
        comment.dislikes.add(request.user)
        # Remove like if exists
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
    
    # Redirect back to the post detail page
    return HttpResponseRedirect(reverse('post_details', args=[str(comment.post.pk)]))