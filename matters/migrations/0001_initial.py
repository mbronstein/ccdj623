# Generated by Django 4.0.5 on 2022-06-25 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('case_id', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('open_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_matters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
