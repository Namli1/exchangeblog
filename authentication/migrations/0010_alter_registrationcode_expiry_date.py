# Generated by Django 3.2 on 2021-07-03 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_registrationcode_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationcode',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 2, 12, 34, 53, 960126), help_text='The date upon which this code will be invalid, is automatically populated, but you can adjust it if you want.', verbose_name='Expiry date'),
        ),
    ]
