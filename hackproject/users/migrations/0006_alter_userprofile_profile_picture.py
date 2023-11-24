# Generated by Django 4.2.4 on 2023-10-09 21:02

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.UserProfile.generate_upload_path, verbose_name='Profile picture'),
        ),
    ]