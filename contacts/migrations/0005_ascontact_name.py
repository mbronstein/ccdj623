# Generated by Django 4.0.5 on 2022-07-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_ascontact_options_remove_ascontact_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ascontact',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
