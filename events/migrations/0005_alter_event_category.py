# Generated by Django 4.0.5 on 2022-07-12 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_eventcategory_options_remove_event_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_event_categories', to='events.eventcategory'),
        ),
    ]