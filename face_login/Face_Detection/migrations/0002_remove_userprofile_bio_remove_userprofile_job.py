# Generated by Django 4.1.5 on 2023-01-24 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Detection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='job',
        ),
    ]
