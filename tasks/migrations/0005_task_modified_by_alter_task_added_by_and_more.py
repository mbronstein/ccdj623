# Generated by Django 4.0.5 on 2022-07-31 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_rename_created_by_task_added_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='taskcategory',
            name='type',
            field=models.IntegerField(choices=[(1, 'Unknown'), (2, 'Call'), (3, 'Wait'), (4, 'Email'), (5, 'Draft'), (6, 'Review'), (7, 'Send'), (8, 'Other'), (9, 'Pay Bill'), (10, 'Prepare Bill'), (11, 'Research'), (12, 'Fix'), (13, 'Send Fax')], default=1),
        ),
    ]