from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #Optional summary or teaser visible on the main page.
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} || {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.RESTRICT, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        #Limit the length of the comment to 40 characters. Append '...' if the comment is longer than 40 characters.
        return f"{self.author} commented: {self.body[:40]}{'...' if len(self.body) > 40 else ''}"
    