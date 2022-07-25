# Generated by Django 4.0.5 on 2022-07-25 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matters', '0002_matter'),
        ('events', '0003_remove_event_matter'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='matter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_matters', to='matters.matter'),
        ),
    ]
