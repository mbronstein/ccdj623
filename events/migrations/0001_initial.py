# Generated by Django 4.0.5 on 2022-07-28 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
        ('matters', '0003_remove_matter_assigned_to_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
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
                ('type', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Call'), (3, 'Conference'), (4, 'Deadline'), (5, 'Video Conf'), (6, 'Hearing'), (7, 'Meeting'), (8, 'Presentation'), (9, 'Other'), (10, 'Deadline Warning')], default=1)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'event categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(default=30)),
                ('attendees', models.CharField(blank=True, max_length=60, null=True)),
                ('location', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Pending'), (3, 'Cancelled'), (4, 'Done'), (5, 'On Hold'), (6, 'Other'), (7, 'Wait to be rescheduled')], default=2)),
                ('priority', models.PositiveIntegerField(default=0)),
                ('assigned_to', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_event_categories', to='events.eventcategory')),
                ('matter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_matters', to='matters.matter')),
            ],
        ),
    ]
