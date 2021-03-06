# Generated by Django 4.0.5 on 2022-07-31 14:47

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matters', '0003_remove_matter_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matter',
            name='datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='matter',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mattertype',
            name='datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='mattertype',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
