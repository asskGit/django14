# Generated by Django 5.0.6 on 2024-05-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
