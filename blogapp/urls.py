from django.urls import path
from .views import HomeView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),                                  #Call as_view() method to return a callable view that takes a request and returns a response.
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details'),       #Use Primary Key to denote a specific post.
]
