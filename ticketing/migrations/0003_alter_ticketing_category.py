# Generated by Django 4.0.4 on 2022-06-30 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_ticketing_alter_responseticket_tickets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketing',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='ticketing.category'),
        ),
    ]
