from django.contrib import admin
from .models import Post, Category, UserProfile, Comment, FeaturedPost

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(FeaturedPost)