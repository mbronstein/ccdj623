# Generated by Django 4.0.5 on 2022-07-19 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='KbEntryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Link'), (3, 'How To'), (4, 'Other')], default=1)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('files_foldername', models.CharField(blank=True, max_length=80, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kbcategories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'KBase categories',
            },
        ),
        migrations.CreateModel(
            name='KbEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=30)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_kbentries', to='kbentries.kbentrycategory')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kb_created_by', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]