import uuid
import taggit

from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
UserModel = get_user_model()


class MatterType(models.Model):
    id=models.BigAutoField
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        UserModel,
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
    name = models.CharField(max_length=150)
    case_id = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(MatterType,
                             default=1,
                             on_delete=models.CASCADE,
                             related_name="types_matters")
    tags = TaggableManager(blank=True)
    created_by = models.ForeignKey(
        UserModel,
        default=1,
        on_delete=models.CASCADE,
        related_name="user_matters"
    )
    open_date = models.DateField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return self.name