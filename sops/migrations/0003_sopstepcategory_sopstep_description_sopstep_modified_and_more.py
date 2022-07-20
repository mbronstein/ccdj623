# Generated by Django 4.0.5 on 2022-07-20 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sops', '0002_sop_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SopStepCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Call'), (3, 'Email'), (4, 'Fill Form'), (5, 'Draft'), (6, 'Review'), (7, 'Wait')], default=1)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sop_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SOP categories',
            },
        ),
        migrations.AddField(
            model_name='sopstep',
            name='description',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='sopstep',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='sop',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='sopstep',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sopstep',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='SopCategory',
        ),
        migrations.AddField(
            model_name='sopstep',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_steps', to='sops.sopstepcategory'),
        ),
    ]
