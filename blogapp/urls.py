from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView, CategoryView, PostLikeView, PostDislikeView, CommentLikeView, CommentDislikeView, add_comment, edit_comment, delete_comment

urlpatterns = [
    path('', HomeView.as_view(), name='home'),                                      #Call as_view() method to return a callable view that takes a request and returns a response.
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details'),           #Use Primary Key to denote a specific post.
    path('new_post/', CreatePostView.as_view(), name='create_post'),                #Create a new post.
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),         #Update an existing post.
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),     #Delete an existing post.
    path('category/<str:cat>', CategoryView, name='category'),                      #Filter posts by category.
    path('post/like/<int:pk>', PostLikeView, name='post_like'),                     #Like a post.
    path('post/dislike/<int:pk>', PostDislikeView, name='post_dislike'),            #Dislike a post.
    path('comment/like/<int:pk>', CommentLikeView, name='comment_like'),            #Like a comment.
    path('comment/dislike/<int:pk>', CommentDislikeView, name='comment_dislike'),   #Dislike a comment.
    path('comment/add/<int:pk>/', add_comment, name='add_comment'),                 #Add a comment.  
    path('comment/edit/<int:pk>/', edit_comment, name='edit_comment'),              #Edit a comment.
    path('comment/delete/<int:pk>/', delete_comment, name='delete_comment'),        #Delete a comment.
]
