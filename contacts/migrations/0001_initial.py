# Generated by Django 4.0.5 on 2022-07-27 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('state', models.CharField(blank=True, max_length=80, null=True)),
                ('country', models.CharField(blank=True, max_length=80, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.CharField(blank=True, max_length=80, null=True)),
                ('phone', models.CharField(blank=True, max_length=80, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
