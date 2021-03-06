# Generated by Django 4.0.5 on 2022-07-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sops', '0003_sopstepcategory_sopstep_description_sopstep_modified_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sopstep',
            options={'verbose_name_plural': 'SOP Steps'},
        ),
        migrations.AlterModelOptions(
            name='sopstepcategory',
            options={'verbose_name_plural': 'SOP Step categories'},
        ),
        migrations.RemoveField(
            model_name='sopstepcategory',
            name='url',
        ),
        migrations.AddField(
            model_name='sopstep',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
