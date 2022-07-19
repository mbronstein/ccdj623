import uuid
import taggit

from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager

USER_MODEL = get_user_model()


# Create your models here.


class MatterType(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_mattertypes"
    )
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'matters'


class Matter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True)
    case_id = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(MatterType,
                             default=1,
                             on_delete=models.CASCADE,
                             related_name="types_matters")
    files_foldername = models.CharField(max_length=80,
                                        default=name)
    tags = TaggableManager(blank=True)
    created_by = models.ForeignKey(
        USER_MODEL,
        default=1,
        on_delete=models.CASCADE,
        related_name="user_matters"
    )
    open_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
