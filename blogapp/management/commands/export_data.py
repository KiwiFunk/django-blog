from django.core.management.base import BaseCommand
from django.core import serializers
from django.contrib.auth.models import User
from blogapp.models import Post, Category, Comment, UserProfile  # Updated import
import json
import os

class Command(BaseCommand):
    """
    Command for backing up our local database to JSON files.
    """
    help = 'Exports data to JSON files with proper UTF-8 encoding'

    def handle(self, *args, **options):
        # Create backups directory if it doesn't exist
        if not os.path.exists('backups'):
            os.makedirs('backups')

        # Export User data
        users_data = serializers.serialize('json', User.objects.all(), 
                                         use_natural_foreign_keys=True,
                                         use_natural_primary_keys=True)
        with open('backups/users.json', 'w', encoding='utf-8') as f:
            f.write(users_data)
        self.stdout.write(self.style.SUCCESS('Users exported successfully'))

        # Export UserProfile data
        profiles_data = serializers.serialize('json', UserProfile.objects.all(),
                                            use_natural_foreign_keys=True,
                                            use_natural_primary_keys=True)
        with open('backups/profiles.json', 'w', encoding='utf-8') as f:
            f.write(profiles_data)
        self.stdout.write(self.style.SUCCESS('UserProfiles exported successfully'))

        # Export Category data
        categories_data = serializers.serialize('json', Category.objects.all(),
                                              use_natural_foreign_keys=True,
                                              use_natural_primary_keys=True)
        with open('backups/categories.json', 'w', encoding='utf-8') as f:
            f.write(categories_data)
        self.stdout.write(self.style.SUCCESS('Categories exported successfully'))

        # Export Post data
        posts_data = serializers.serialize('json', Post.objects.all(),
                                         use_natural_foreign_keys=True,
                                         use_natural_primary_keys=True)
        with open('backups/posts.json', 'w', encoding='utf-8') as f:
            f.write(posts_data)
        self.stdout.write(self.style.SUCCESS('Posts exported successfully'))

        # Export Comment data
        comments_data = serializers.serialize('json', Comment.objects.all(),
                                            use_natural_foreign_keys=True,
                                            use_natural_primary_keys=True)
        with open('backups/comments.json', 'w', encoding='utf-8') as f:
            f.write(comments_data)
        self.stdout.write(self.style.SUCCESS('Comments exported successfully'))