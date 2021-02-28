# Generated by Django 3.1.1 on 2021-01-17 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchangeblog', '0003_auto_20201222_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
