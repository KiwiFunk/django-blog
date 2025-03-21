from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)                        # The title of the post.                
    author = models.ForeignKey(User, on_delete=models.CASCADE)      # User that created the post. When the user is deleted, their posts are also deleted to prevent orphaned data.
    body = models.TextField()                                       # The body of the post. e.g the content.
    created_at = models.DateTimeField(auto_now_add=True)            # The date and time the post was created.           

    def __str__(self):
        return self.title + ' | ' + self.author                     # Assign a string representation for each post object. This will be used in the admin panel. This will show the title of the post and the author's username.