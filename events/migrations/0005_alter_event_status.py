# Generated by Django 4.0.5 on 2022-07-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_matter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.IntegerField(choices=[(1, 'Unknown'), (2, 'Pending'), (3, 'Cancelled'), (4, 'Done'), (5, 'On Hold'), (6, 'Other'), (7, 'Wait to be rescheduled')], default=2),
        ),
    ]
