from django.core.management.base import BaseCommand
from blogapp.models import Post, UserProfile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Checks current image paths in database'

    def handle(self, *args, **options):
        self.stdout.write("\nBlog Post Images:")
        self.stdout.write("-" * 50)
        posts = Post.objects.all()
        for post in posts:
            self.stdout.write(f"Post: {post.title}")
            self.stdout.write(f"Image name: {post.header_image.name}")
            self.stdout.write(f"Image URL: {post.header_image.url if post.header_image else 'No image'}")
            self.stdout.write("-" * 50)

        self.stdout.write("\nProfile Pictures:")
        self.stdout.write("-" * 50)
        users = User.objects.all()
        for user in users:
            if hasattr(user, 'userprofile'):
                self.stdout.write(f"User: {user.username}")
                self.stdout.write(f"Image name: {user.userprofile.profile_pic.name if user.userprofile.profile_pic else 'No image'}")
                self.stdout.write(f"Image URL: {user.userprofile.profile_pic.url if user.userprofile.profile_pic else 'No image'}")
                self.stdout.write("-" * 50)