# Generated by Django 3.2.9 on 2022-02-27 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='cat', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Image Name', max_length=1000)),
                ('description', models.TextField(default='Body')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('ProfileItems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Image Name', max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/postsImage')),
            ],
        ),
        migrations.CreateModel(
            name='Replyes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Image Name', max_length=1000)),
                ('description', models.TextField(default='Body')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('ProfileItems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('users', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Post Title', max_length=1000)),
                ('description', models.TextField(default='Body')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='media/postsImage')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('post_category_str', models.CharField(default='Post Title', max_length=1000)),
                ('ProfileItems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('auhtor', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(blank=True, null=True, related_name='Comments', to='postsApi.Comments')),
                ('images', models.ManyToManyField(blank=True, null=True, related_name='images', to='postsApi.Image')),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('post_category', models.ManyToManyField(blank=True, null=True, related_name='Category', to='postsApi.Category')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='replyes',
            field=models.ManyToManyField(blank=True, null=True, related_name='Replyes', to='postsApi.Replyes'),
        ),
        migrations.AddField(
            model_name='comments',
            name='users',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
