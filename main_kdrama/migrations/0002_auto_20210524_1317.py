# Generated by Django 3.2 on 2021-05-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_kdrama', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ruchit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catgory', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='categories',
        ),
    ]
