# Generated by Django 5.1.7 on 2025-03-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_remove_post_tite_tag_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(),
        ),
    ]
