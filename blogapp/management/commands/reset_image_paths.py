from django.core.management.base import BaseCommand
from blogapp.models import Post, UserProfile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Resets all image paths to their original values'

    def handle(self, *args, **options):
        # Reset blog post images
        posts = Post.objects.all()
        for post in posts:
            try:
                if post.header_image:
                    # Reset to original path
                    original_name = post.title.lower().replace(' ', '-')
                    self.stdout.write(f"Current image path: {post.header_image.name}")
                    self.stdout.write(f"Enter the correct filename for post '{post.title}' (including extension): ")
                    new_filename = input()
                    post.header_image.name = f'images/{new_filename}'
                    post.save()
                    self.stdout.write(
                        self.style.SUCCESS(f'Reset image for post: {post.title} to {post.header_image.name}')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to reset image for post {post.title}: {str(e)}')
                )

        # Reset profile pictures
        users = User.objects.all()
        for user in users:
            try:
                if hasattr(user, 'userprofile') and user.userprofile.profile_pic:
                    self.stdout.write(f"Current profile image path: {user.userprofile.profile_pic.name}")
                    self.stdout.write(f"Enter the correct filename for user '{user.username}' (including extension): ")
                    new_filename = input()
                    user.userprofile.profile_pic.name = f'images/profile/{new_filename}'
                    user.userprofile.save()
                    self.stdout.write(
                        self.style.SUCCESS(f'Reset profile pic for user: {user.username} to {user.userprofile.profile_pic.name}')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to reset profile pic for {user.username}: {str(e)}')
                )