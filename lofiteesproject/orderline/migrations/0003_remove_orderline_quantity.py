# Generated by Django 3.0.6 on 2020-09-12 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderline', '0002_auto_20200912_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='quantity',
        ),
    ]
