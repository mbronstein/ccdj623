# Generated by Django 4.0.5 on 2022-07-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Attendees',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]