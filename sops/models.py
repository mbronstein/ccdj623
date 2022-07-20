from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

USER_MODEL = get_user_model()


class SopStepCategory(models.Model):
    class SopStepCategoryTypeChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Unknown'
        CALL = 2, 'Call'
        EMAIL = 3, 'Email'
        FILL_FORM = 4, 'Fill Form'
        DRAFT = 5, 'Draft'
        REVIEW = 6, 'Review'
        WAIT = 7, 'Wait'

    id = models.BigAutoField
    type = models.IntegerField(choices=SopStepCategoryTypeChoices.choices,
                               default=SopStepCategoryTypeChoices.UNKNOWN)
    name = models.CharField(max_length=150,
                            unique=True)
    url = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=60,
                                   null=True,
                                   blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    created_by = models.ForeignKey(USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="user_sop_categories"
                                   )
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'sops'
        verbose_name_plural = "SOP categories"


class SopStep(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=30,
                            null=True
                            )
    category = models.ForeignKey('SopStepCategory',
                                 null=True,
                                 related_name="categories_steps",
                                 on_delete=models.CASCADE
                                 )
    last_updated = models.DateTimeField(auto_now_add=True)

    description = models.CharField(max_length=80,
                                   blank=True)

    notes = models.TextField(blank=True,
                             null=True,
                             )
    tags = TaggableManager(blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="user_sopsteps",
                                   on_delete=models.CASCADE,
                                   )
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'sops'
        verbose_name_plural = "SOPs"

    def __str__(self):
        return f"{self.title})"


class Sop(models.Model):
    title = models.CharField(max_length=80)
    # category = models.ForeignKey('sops.SopCategory',
    #                              # default=SOPCategory.objects.get(pk=1),
    #                              null=True,
    #                              on_delete=models.CASCADE,
    #                              related_name="categories_sops")
    slug = models.SlugField(max_length=30)
    description = models.CharField(max_length=80, null=True, blank=True)

    created_date = models.DateField(default=timezone.now)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="users_sops",
                                   on_delete=models.CASCADE,
                                   )
    last_updated = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True,
                             null=True,
                             )
    tags = TaggableManager(blank=True)
    steps = models.ForeignKey("Sop", null=True,
                              on_delete=models.DO_NOTHING,
                              related_name='sop_steps'
                              )

    class Meta:
        app_label = 'sops'
        verbose_name_plural = "SOPs"

    def __str__(self):
        return f"{self.title}"
