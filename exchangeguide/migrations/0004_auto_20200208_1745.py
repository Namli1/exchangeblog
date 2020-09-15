# Generated by Django 2.2.4 on 2020-02-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeguide', '0003_auto_20200207_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countryguidepost',
            name='thumbnail_picture',
        ),
        migrations.AlterField(
            model_name='countryguidepost',
            name='guide_language',
            field=models.CharField(choices=[('EN', 'English'), ('DE', 'Deutsch'), ('IT', 'Italiano'), ('FR', 'Français')], default='EN', help_text='Please select the language you will use for the post.', max_length=2),
        ),
    ]
