# Generated by Django 4.0.5 on 2022-07-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='code',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
