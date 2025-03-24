from django.core.management.base import BaseCommand
from blogapp.models import Post, UserProfile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Updates Cloudinary paths to use project folder structure'

    def handle(self, *args, **options):
        # Update blog post images
        posts = Post.objects.all()
        for post in posts:
            if post.header_image:
                current_path = post.header_image.name
                if not current_path.startswith('django-blog/'):
                    # Extract filename from current path
                    filename = current_path.split('/')[-1]
                    # Update to new path structure
                    new_path = f'django-blog/blog_posts/{filename}'
                    post.header_image.name = new_path
                    post.save()
                    self.stdout.write(
                        self.style.SUCCESS(f'Updated post image: {current_path} -> {new_path}')
                    )

        # Update profile pictures
        users = User.objects.all()
        for user in users:
            if hasattr(user, 'userprofile') and user.userprofile.profile_pic:
                current_path = user.userprofile.profile_pic.name
                if not current_path.startswith('django-blog/'):
                    # Extract filename from current path
                    filename = current_path.split('/')[-1]
                    # Update to new path structure
                    new_path = f'django-blog/profile_pics/{filename}'
                    user.userprofile.profile_pic.name = new_path
                    user.userprofile.save()
                    self.stdout.write(
                        self.style.SUCCESS(f'Updated profile pic: {current_path} -> {new_path}')
                    )