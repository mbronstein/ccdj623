from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from core.models import BaseModelMixin
from taggit.managers import TaggableManager

USER_MODEL = get_user_model()


class KbEntryCategory(BaseModelMixin):
    class KbaseTypeChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Unknown'
        LINK = 2, 'Link'
        HOWTO = 3, 'How To'
        OTHER = 4, 'Other'

    type = models.IntegerField(choices=KbaseTypeChoices.choices,
                               default=KbaseTypeChoices.UNKNOWN)


    def __str__(self):
        return self.title

    class Meta:
        app_label = 'kbentries'
        verbose_name_plural = "KBase categories"


#
#
# class HowtoStep(models.model):
#     slug = models.SlugField(max_length=30, null=True)
#     title = models.CharField(max_length=50)


class KbEntry(BaseModelMixin):
    category = models.ForeignKey('KbEntryCategory',
                                 # default=KbaseCategory.objects.get(pk=1),
                                 null=True,
                                 on_delete=models.CASCADE,
                                 related_name="categories_kbentries")
    url1 = models.URLField(null=True, blank=True)
    url2 = models.URLField(null=True, blank=True)

    class Meta:
        app_label = 'kbentries'
        verbose_name_plural = "KBase entries"

    def __str__(self):
        return f"{self.title})"
