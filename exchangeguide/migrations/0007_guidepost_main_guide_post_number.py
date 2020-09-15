# Generated by Django 2.2.4 on 2020-02-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeguide', '0006_auto_20200216_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidepost',
            name='main_guide_post_number',
            field=models.IntegerField(blank=True, help_text='If post is part of the main step by step guide, enter its number in the order here.', null=True, unique=True),
        ),
    ]
