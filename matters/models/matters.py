import uuid
import taggit

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Matter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    case_id = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    case_type =
    # tags = models.  #todo finish
    created_by = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="user_matters"
     )
    open_date = models.DateField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return self.name
