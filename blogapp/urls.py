from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),          #Call as_view() method to return a callable view that takes a request and returns a response.
]
