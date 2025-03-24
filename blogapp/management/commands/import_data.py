from django.core.management.base import BaseCommand
from django.db import transaction

class Command(BaseCommand):
    help = 'Imports data from JSON backups in the correct order'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Delete existing data
                self.stdout.write("Clearing existing data...")
                from django.contrib.auth.models import User
                from blogapp.models import UserProfile, Category, Post, Comment
                
                Comment.objects.all().delete()
                Post.objects.all().delete()
                Category.objects.all().delete()
                UserProfile.objects.all().delete()
                User.objects.exclude(is_superuser=True).delete()

                # Load data in order
                self.stdout.write("Loading users...")
                self.run_loaddata('backups/users.json')

                self.stdout.write("Loading categories...")
                self.run_loaddata('backups/categories.json')

                self.stdout.write("Loading posts...")
                self.run_loaddata('backups/posts.json')

                self.stdout.write("Loading comments...")
                self.run_loaddata('backups/comments.json')

                self.stdout.write(self.style.SUCCESS('Successfully imported all data'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during import: {str(e)}'))

    def run_loaddata(self, fixture_path):
        from django.core.management import call_command
        try:
            call_command('loaddata', fixture_path, verbosity=0)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading {fixture_path}: {str(e)}'))
            raise