# Generated by Django 4.0.5 on 2022-07-13 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matters', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('type', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Call'), (3, 'Conference'), (4, 'Deadline'), (5, 'Video Conf'), (6, 'OHO Hearing'), (7, 'Meeting'), (8, 'Presentation'), (9, 'Other'), (10, 'Deadline Warning')], default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_event_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'event categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('startdatetime', models.DateTimeField(null=True)),
                ('length', models.IntegerField(default=30)),
                ('attendees', models.CharField(blank=True, max_length=60, null=True)),
                ('location', models.CharField(blank=True, max_length=40, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('note', models.TextField(blank=True, null=True)),
                ('priority', models.PositiveIntegerField(default=0)),
                ('assigned_to', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_event_categories', to='events.eventcategory')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_created_by', to=settings.AUTH_USER_MODEL)),
                ('matter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_matters', to='matters.matter')),
            ],
            options={
                'ordering': ['priority', 'created_date'],
            },
        ),
    ]
