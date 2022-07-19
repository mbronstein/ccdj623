from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import  models
from django.utils import timezone
from taggit.managers import TaggableManager

USER_MODEL = get_user_model()


class KbEntryCategory(models.Model):
    class KbaseTypeChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Unknown'
        LINK = 2, 'Link'
        HOWTO = 3, 'How To'
        OTHER = 4, 'Other'

    id = models.BigAutoField

    type = models.IntegerField(choices=KbaseTypeChoices.choices,
                               default=KbaseTypeChoices.UNKNOWN)
    name = models.CharField(max_length=150,
                            unique=True)
    url = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=60,
                                   null=True,
                                   blank=True)
    files_foldername = models.CharField(max_length=80,
                                        null=True,
                                        blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    created_by = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name= "user_kbcategories"
    )
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'kbentries'
        verbose_name_plural = "KBase categories"


class KbEntry(models.Model):
    title = models.CharField(max_length=80)
    category = models.ForeignKey('kbentries.KbEntryCategory',
                                 # default=KbaseCategory.objects.get(pk=1),
                                 null=True,
                                 on_delete=models.CASCADE,
                                 related_name="categories_kbentries")
    slug = models.SlugField(max_length=30 )

    created_date = models.DateField(default=timezone.now)

    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True,
                                      null=True
                                      )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="user_kb_created_by",
                                   on_delete=models.CASCADE,

                                   )

    notes = models.TextField(blank=True,
                            null=True,
                            )
    tags = TaggableManager()
    last_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'kbentries'

    def __str__(self):
        return f"{self.title}({self.category.name})"
