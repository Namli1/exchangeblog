# Generated by Django 3.1.1 on 2021-03-08 20:12

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeblog', '0005_auto_20210204_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blogcontent',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
