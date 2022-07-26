# Generated by Django 4.0.5 on 2022-07-26 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matters', '0003_remove_matter_assigned_to_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Note'), (3, 'Call'), (4, 'Email'), (5, 'SMS'), (6, 'Document'), (7, 'Other'), (8, 'Voicemail'), (9, 'Dictation'), (10, 'Form')], default=1)),
            ],
            options={
                'verbose_name_plural': 'entry categories',
            },
        ),
        migrations.CreateModel(
            name='CaseEntry',
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
                ('time_spent', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='entries.entrycategory')),
                ('matter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matters', to='matters.matter')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'case entry',
                'verbose_name_plural': 'case entries',
            },
        ),
    ]
