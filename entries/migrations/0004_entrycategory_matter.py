# Generated by Django 4.0.5 on 2022-07-25 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matters', '0002_matter'),
        ('entries', '0003_remove_caseentry_matter'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrycategory',
            name='matter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matter_entries', to='matters.matter'),
        ),
    ]