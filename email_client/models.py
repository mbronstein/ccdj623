
from django.contrib.auth import get_user_model
from django.db import models
from core.models import BaseModelMixin
import django.utils.timezone
# from django.utils import timezone

from taggit.managers import TaggableManager
from phonenumber_field.modelfields import PhoneNumberField
from matters.models import Matter
from model_utils.managers import InheritanceManager

from django.utils import timezone

USER_MODEL = get_user_model()


class MailForm(BaseModelMixin):
    type = models.IntegerField(choices=EntryTypeChoices.choices,
                               default=EntryTypeChoices.UNKNOWN)
    matter = models.ForeignKey(Matter,
                               null=True,
                               related_name="matter_entries",
                               on_delete=models.CASCADE
                               )
    name = models.CharField(max_length=40,
                            unique=True)
    description = models.CharField(max_length=80,
                                   null=True,
                                   blank=True)
    notes = models.TextField(null=True, blank=True)

    edited_by = models.ForeignKey(USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name="user_entries"
                                  )
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.type}"

    class Meta:
        app_label = 'entries'
        verbose_name_plural = "entry categories"


def filefolder_name(instance, filename):
    return instance.matter.files_foldername


class CaseEntry(models.Model):
    id = models.BigAutoField
    datetime = models.DateTimeField(default=timezone.now, blank=True)
    title = models.CharField(max_length=60)
    category = models.ForeignKey('entries.EntryCategory',
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE,
                                 related_name='categories'
                                 )
    matter = models.ForeignKey("matters.Matter",
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='matters',
                               )

    file = models.FileField(upload_to=filefolder_name,
                            null=True,
                            blank=True)

    description = models.CharField(max_length=100,
                                   null=True,
                                   blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    tags = TaggableManager(blank=True)
    time_spent = models.DecimalField(default=0,
                                     decimal_places=1,
                                     max_digits=3)
    created_by = models.ForeignKey(USER_MODEL,
                                   on_delete=models.CASCADE,
                                   )
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'entries'
        verbose_name = 'case entry'
        verbose_name_plural = 'case entries'

    def __str__(self):
        return f"{self.title}"

    # for admin display
    def compact_datetime(self):
        return self.datetime.strftime("%m/%d/%y %I:%M %p (%a)")

    compact_datetime.short_description = 'Date/Time'

    def file_folder_name(instance, filename):
        return self.matter.title
