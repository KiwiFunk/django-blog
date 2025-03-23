from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

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

class UserProfile(models.Model):
    """
    This model extends the default User model provided by Django. 
    We can add additional fields to the user model by creating a one-to-one relationship with the User model.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)      # A one-to-one relationship with the User model. When the user is deleted, their profile is also deleted to prevent orphaned data.
    bio = models.TextField()                                                    # A brief bio of the user.
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/') # The profile picture of the user. (Optional)
    website_url = models.CharField(max_length=255, null=True, blank=True)       # The user's website URL. (Optional)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)       # The user's Twitter URL. (Optional)
    github_url = models.CharField(max_length=255, null=True, blank=True)        # The user's GitHub URL. (Optional)
    artstation_url = models.CharField(max_length=255, null=True, blank=True)    # The user's ArtStation URL. (Optional)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)      # The user's LinkedIn URL. (Optional)

    def __str__(self):
        return str(self.user)                                               # Assign a string representation for each user profile object. This will be used in the admin panel.

    def get_absolute_url(self):
        return reverse('home')     
    
    def clean(self):
        """
        Clean the website URL field to ensure it is a valid URL.
        """
        validator = URLValidator()
        if self.website_url and not self.website_url.startswith(('http://', 'https://')):
            self.website_url = 'https://' + self.website_url
        try:
            if self.website_url:
                validator(self.website_url)
        except ValidationError:
            raise ValidationError({'website_url': 'Enter a valid URL.'})                                         # Redirect to the home page after creating a new user profile.

class Post(models.Model):
    title = models.CharField(max_length=255)                                    # The title of the post.
    title_tag = models.CharField(max_length=100, blank=True, null=True)         # A tagline for the post. (Optional)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')# The header image for the post. (Optional)
    author = models.ForeignKey(User, on_delete=models.CASCADE)                  # User that created the post. When the user is deleted, their posts are also deleted to prevent orphaned data.
    summary = models.TextField(blank=True, null=True)                           # A brief summary of the post to be displayed in the feed. (Optional)
    body = models.TextField(blank=True, null=True)                              # The body of the post. e.g the content.
    created_at = models.DateTimeField(auto_now_add=True)                        # The date and time the post was created.     
    category = models.CharField(max_length=255, default='Uncategorized')        # The category of the post.
    likes = models.ManyToManyField(User, related_name='blog_posts')             # Users that liked the post. A user can like multiple posts & a post can be liked by multiple users. == ManyToMany relationship.   
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
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)   # The post that the comment belongs to. When the post is deleted, the comments are also deleted to prevent orphaned data.
    user = models.ForeignKey(User, on_delete=models.CASCADE)                            # The user that created the comment. When the user is deleted, their comments are also deleted to prevent orphaned data.
    body = models.TextField()                                                           # The body of the comment.
    created_at = models.DateTimeField(auto_now_add=True)                                # The date and time the comment was created.
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)      # Users that liked the comment. A user can like multiple comments & a comment can be liked by multiple users. == ManyToMany relationship.
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)# Users that disliked the comment.

    def total_likes(self):
        return self.likes.count()                                                       # Return the total number of likes for the comment.
    
    def total_dislikes(self):
        return self.dislikes.count()                                                    # Return the total number of dislikes for the comment.
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.user)                                  # Assign a string representation for each comment object. This will be used in the admin panel.