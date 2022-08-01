# -*- coding: utf-8 -*-

from django.db import models
import nanoid
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone
from ckeditor.fields import RichTextField

USER_MODEL = get_user_model()


def generate():
    return nanoid.generate(alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                           size=15)


class BaseModelMixin(models.Model):
    id = models.BigAutoField

    # adapted from https://github.com/willywongi/django-jables/blob/main/jables/models.py

    # nanoid = models.CharField(max_length=21,
    #                             primary_key=True,
    #                             default=generate,
    #                             editable=False)

    title = models.CharField(max_length=255,
                             null=True,
                             blank=True)
    slug = models.SlugField(blank=True,
                            null=True
                            )

    description = models.TextField(blank=True,
                                   null=True)
    datetime = models.DateTimeField(blank=True, null=True,
                                    default=timezone.now)
    notes = RichTextField(null=True, blank=True)
    tags = TaggableManager(blank=True)

    status = models.IntegerField(default=1)
    priority = models.IntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True,
                                   )
    modified = models.DateTimeField(auto_now_add=True,
                                    )

    added_by = models.ForeignKey(USER_MODEL, blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='+',
                                 )
    modified_by = models.ForeignKey(USER_MODEL, blank=True,
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    related_name='+',
                                    )

    def compact_dow_datetime(self):
        if self.datetime is not None:
            return self.datetime.strftime("%m/%d/%y %I:%M %p  (%a)")
        else:
            return "???"

    @property
    def compact_datetime(self):
        if self.datetime is not None:
            return self.datetime.strftime("%m/%d/%y %I:%M %p")
        else:
            return "???"

    def compact_dow_date(self):
        if self.datetime is not None:
            return self.datetime.strftime("%m/%d/%y %I:%M %p (%a)")
        else:
            return "???"

    def compact_date(self):
        if self.datetime is not None:
            return self.datetime.strftime("%m/%d/%y")
        else:
            return "???"

    class Meta:
        app_label = 'core'
        get_latest_by = True
        ordering = ['datetime']
        abstract = True

# class VeryBaseModel(models.Model):
#     delete_flag = models.BooleanField(default=False
#                                       )
#     is_active = models.BooleanField(default=False
#                                     )
#     created = models.DateTimeField(auto_now_add=True,
#                                   )
#     modified = models.DateTimeField(auto_now_add=True,
#                                     )
#     created_by = models.ForeignKey(USER_MODEL,
#                                  blank=True,
#                                  null=True,
#                                  on_delete=models.SET_NULL,
#                                  related_name='+',
#                                  # default=USER_MODEL.objects.get(username='admin')
#                                  )
#     modified_by = models.ForeignKey(USER_MODEL,
#                                     blank=True,
#                                     null=True,
#                                     on_delete=models.SET_NULL,
#                                     related_name='+',
#                                     # default=USER_MODEL.objects.get(username='admin'),
#
#                                     )
#
#
#     class Meta:
#         abstract = True
#         app_label = "email_client"
#


# def save(self, **kwargs):

#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             # Only set added_by during the first save.
#             obj.added_by = request.user
#         super().save(request, obj, form, change)

#
#
# class ActivatorQuerySet(models.query.QuerySet):
#     """
#     ActivatorQuerySet
#     Query set that returns statused results
#     """
#
#     def active(self):
#         """ Return active query set """
#         return self.filter(status=ActivatorModel.ACTIVE_STATUS)
#
#     def inactive(self):
#         """ Return inactive query set """
#         return self.filter(status=ActivatorModel.INACTIVE_STATUS)
#
#
# class ActivatorModelManager(models.Manager):
#     """
#     ActivatorModelManager
#     Manager to return instances of ActivatorModel: SomeModel.objects.active() / .inactive()
#     """
#
#     def get_queryset(self):
#         """ Use ActivatorQuerySet for all results """
#         return ActivatorQuerySet(model=self.model, using=self._db)
#
#     def active(self):
#         """
#         Return active instances of ActivatorModel:
#         SomeModel.objects.active(), proxy to ActivatorQuerySet.active
#         """
#         return self.get_queryset().active()
#
#     def inactive(self):
#         """
#         Return inactive instances of ActivatorModel:
#         SomeModel.objects.inactive(), proxy to ActivatorQuerySet.inactive
#         """
#         return self.get_queryset().inactive()
#
#
# class ActivatorModel(models.Model):
#     """
#     ActivatorModel
#     An abstract base class model that provides activate and deactivate fields.
#     """
#
#     INACTIVE_STATUS = 0
#     ACTIVE_STATUS = 1
#
#     STATUS_CHOICES = (
#         (INACTIVE_STATUS, _('Inactive')),
#         (ACTIVE_STATUS, _('Active')),
#     )
#     status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=ACTIVE_STATUS)
#     activate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for an immediate activation'))
#     deactivate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for indefinite activation'))
#     objects = ActivatorModelManager()
#
#     class Meta:
#         ordering = ('status', '-activate_date',)
#         abstract = True
#
#     def save(self, *args, **kwargs):
#         if not self.activate_date:
#             self.activate_date = now()
#         super().save(*args, **kwargs)
