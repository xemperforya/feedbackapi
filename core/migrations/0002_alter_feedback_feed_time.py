# Generated by Django 3.2.4 on 2021-06-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feed_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
