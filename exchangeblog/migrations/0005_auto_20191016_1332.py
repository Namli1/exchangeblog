# Generated by Django 2.2.4 on 2019-10-16 11:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeblog', '0004_auto_20191014_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blogcontent',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]