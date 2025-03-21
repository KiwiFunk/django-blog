from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)                                # The title of the post.
    title_tag = models.CharField(max_length=100, blank=True, null=True)     # A tagline for the post. (Optional)
    author = models.ForeignKey(User, on_delete=models.CASCADE)              # User that created the post. When the user is deleted, their posts are also deleted to prevent orphaned data.
    summary = models.TextField(blank=True, null=True)                       # A brief summary of the post to be displayed in the feed. (Optional)
    body = models.TextField()                                               # The body of the post. e.g the content.
    created_at = models.DateTimeField(auto_now_add=True)                    # The date and time the post was created.           

    # Assign a string representation for each post object. This will be used in the admin panel. 
    # This will show the title of the post and the author's username.
    def __str__(self):
        return self.title + ' | ' + str(self.author) 

    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])                 # Redirect to the post details page after creating a new post.
        