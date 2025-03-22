from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView, CatagoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),                                  #Call as_view() method to return a callable view that takes a request and returns a response.
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details'),       #Use Primary Key to denote a specific post.
    path('new_post/', CreatePostView.as_view(), name='create_post'),            #Create a new post.
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),     #Update an existing post.
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'), #Delete an existing post.
    path('category/<str:category>', HomeView.as_view(), name='category'),       #Filter posts by category.
]
