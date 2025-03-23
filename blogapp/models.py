from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    """
    Categories can be added in the admin panel by superusers. Our create/edit forms will be dynamically populated with the categories.
    """
    class Meta:
        verbose_name_plural = 'categories'                                 # Assign a plural name to prevent default pluralization of the model name. (Catagory(s))

    name = models.CharField(max_length=255)                                # The name of the category.
    
    def __str__(self):
        return self.name                                                    # Assign a string representation for each category object. This will be used in the admin panel.

class Post(models.Model):
    title = models.CharField(max_length=255)                                # The title of the post.
    title_tag = models.CharField(max_length=100, blank=True, null=True)     # A tagline for the post. (Optional)
    author = models.ForeignKey(User, on_delete=models.CASCADE)              # User that created the post. When the user is deleted, their posts are also deleted to prevent orphaned data.
    summary = models.TextField(blank=True, null=True)                       # A brief summary of the post to be displayed in the feed. (Optional)
    body = RichTextField(blank=True, null=True)                             # The body of the post. e.g the content.
    created_at = models.DateTimeField(auto_now_add=True)                    # The date and time the post was created.     
    category = models.CharField(max_length=255, default='Uncategorized')    # The category of the post.
    likes = models.ManyToManyField(User, related_name='blog_posts')         # Users that liked the post. A user can like multiple posts & a post can be liked by multiple users. == ManyToMany relationship.   
    dislikes = models.ManyToManyField(User, related_name='blog_posts_dislikes') # Users that disliked the post.

    def total_likes(self):
        return self.likes.count()                                           # Return the total number of likes for the post.

    def total_dislikes(self):
        return self.dislikes.count()                                        # Return the total number of dislikes for the post.


    # Assign a string representation for each post object. This will be used in the admin panel. 
    # This will show the title of the post and the author's username.
    def __str__(self):
        return self.title + ' | ' + str(self.author) 

    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])                 # Redirect to the post details page after creating a new post.
        