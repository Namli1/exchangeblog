# Generated by Django 2.2.4 on 2019-11-24 02:13

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeblog', '0020_auto_20191124_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail_picture',
            field=imagekit.models.fields.ProcessedImageField(default='thumbnails/IMG_2090.jpeg', upload_to='thumbnails/'),
        ),
    ]
