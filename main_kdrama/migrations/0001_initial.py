# Generated by Django 3.2.7 on 2021-10-06 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category10_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category1_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category2_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category3_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category4_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category5_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category6_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category7_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category8_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_tittle', models.CharField(max_length=300)),
                ('serie_img', models.URLField()),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category9_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='epi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_url', models.CharField(max_length=300)),
                ('epi_no', models.IntegerField()),
                ('epi_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='episodesss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_url', models.CharField(max_length=300)),
                ('onlyepisodenumber', models.IntegerField()),
                ('video_embed', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='main_poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='upload_serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_width1600', models.URLField()),
                ('min_width1440', models.URLField()),
                ('min_width960', models.URLField()),
                ('min_width600', models.URLField()),
                ('img', models.URLField()),
                ('title', models.CharField(max_length=300)),
                ('image_description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('genres', models.CharField(max_length=300)),
                ('cast', models.CharField(max_length=300)),
                ('episodes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usertracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(blank=True, max_length=300, null=True)),
                ('episode_watching', models.CharField(max_length=300)),
                ('img', models.URLField()),
                ('title', models.CharField(max_length=300)),
            ],
        ),
    ]
