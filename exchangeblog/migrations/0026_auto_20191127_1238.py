# Generated by Django 2.2.4 on 2019-11-27 11:38

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeblog', '0025_auto_20191124_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail_picture',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='thumbnails/'),
        ),
    ]