# Generated by Django 4.0.4 on 2022-07-02 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_alter_ticketing_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketing',
            name='phonnum',
        ),
        migrations.AddField(
            model_name='ticketing',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='ticketing',
            name='status',
            field=models.CharField(choices=[(1, 'بررسی شده'), (2, 'درحال بررسی'), (3, 'بررسی نشده')], default='بررسی نشده', max_length=32),
        ),
    ]
