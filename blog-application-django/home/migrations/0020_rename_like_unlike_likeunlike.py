# Generated by Django 4.1.7 on 2023-03-27 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_like_unlike_remove_blogpost_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like_Unlike',
            new_name='LikeUnlike',
        ),
    ]
