# Generated by Django 4.0.5 on 2022-07-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_ascontact_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ascontact',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='ascontact',
            name='name',
        ),
        migrations.AlterField(
            model_name='ascontact',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
