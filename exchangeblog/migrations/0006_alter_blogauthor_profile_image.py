# Generated by Django 3.2 on 2021-07-03 15:40

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeblog', '0005_auto_20210703_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthor',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='static/images/default_profile_image.jpg', help_text='Select a profile image for your account (optional)', upload_to='profile_images/', verbose_name='Profile Image'),
        ),
    ]