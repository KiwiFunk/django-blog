from django.core.management.base import BaseCommand
from django.conf import settings
from blogapp.models import Post, UserProfile
from django.contrib.auth.models import User
import os
import cloudinary
import cloudinary.uploader
from decouple import config

class Command(BaseCommand):
    help = 'Migrates existing images to Cloudinary'
    
    # Define project folder name
    PROJECT_FOLDER = 'django-blog'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configure Cloudinary
        cloudinary.config( 
            cloud_name = config('CLOUDINARY_CLOUD_NAME'),
            api_key = config('CLOUDINARY_API_KEY'),
            api_secret = config('CLOUDINARY_API_SECRET')
        )

    def handle(self, *args, **options):
        # Debug info
        media_root = os.path.normpath(settings.MEDIA_ROOT)
        self.stdout.write(f"MEDIA_ROOT: {media_root}")

        # Migrate blog post images
        posts = Post.objects.all()
        for post in posts:
            if post.header_image and not post.header_image.name.startswith('http'):
                try:
                    image_path = post.header_image.name.replace('/', os.sep)
                    local_path = os.path.normpath(os.path.join(media_root, image_path))
                    
                    self.stdout.write(f"Processing image: {image_path}")
                    
                    if os.path.exists(local_path):
                        # Upload to Cloudinary with project folder structure
                        cloudinary_response = cloudinary.uploader.upload(
                            local_path,
                            folder=f'{self.PROJECT_FOLDER}/blog_posts',  # Updated folder path
                            use_filename=True,
                            unique_filename=True
                        )
                        
                        # Store just the public ID, not the full URL
                        post.header_image.name = cloudinary_response['public_id']
                        post.save()
                        
                        self.stdout.write(
                            self.style.SUCCESS(f'Successfully migrated image for post: {post.title} (ID: {cloudinary_response["public_id"]})')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'File not found: {local_path}')
                        )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Failed to migrate image for post {post.title}: {str(e)}')
                    )

        # Migrate profile pictures
        users = User.objects.all()
        for user in users:
            if hasattr(user, 'userprofile') and user.userprofile.profile_pic and not user.userprofile.profile_pic.name.startswith('http'):
                try:
                    image_path = user.userprofile.profile_pic.name.replace('/', os.sep)
                    local_path = os.path.normpath(os.path.join(media_root, image_path))
                    
                    self.stdout.write(f"Processing profile image: {image_path}")
                    
                    if os.path.exists(local_path):
                        # Upload to Cloudinary with project folder structure
                        cloudinary_response = cloudinary.uploader.upload(
                            local_path,
                            folder=f'{self.PROJECT_FOLDER}/profile_pics',  # Updated folder path
                            use_filename=True,
                            unique_filename=True
                        )
                        
                        # Store just the public ID, not the full URL
                        user.userprofile.profile_pic.name = cloudinary_response['public_id']
                        user.userprofile.save()
                        
                        self.stdout.write(
                            self.style.SUCCESS(f'Successfully migrated profile pic for: {user.username} (ID: {cloudinary_response["public_id"]})')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'File not found: {local_path}')
                        )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Failed to migrate profile pic for {user.username}: {str(e)}')
                    )