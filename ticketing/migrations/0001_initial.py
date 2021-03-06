# Generated by Django 4.0.4 on 2022-06-13 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Ticheting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=32)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'baresi'), (2, 'darhal_baresi'), (3, 'baresi_nashode')], default=3)),
                ('phonnum', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='ticketing.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=32)),
                ('tickets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='ticketing.ticheting')),
            ],
        ),
    ]
