# Generated by Django 3.2.7 on 2021-10-06 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_kdrama', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_serie',
            name='cast',
        ),
        migrations.RemoveField(
            model_name='upload_serie',
            name='image_description',
        ),
        migrations.RemoveField(
            model_name='upload_serie',
            name='year',
        ),
    ]
