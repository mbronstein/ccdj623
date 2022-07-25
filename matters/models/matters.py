import uuid
import taggit

from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager
from core.models import BaseModelMixin
USER_MODEL = get_user_model()


# Create your models here.


class MatterType(BaseModelMixin):
    """type of matter eg SS, LTD, etc.  really parallel to category field
    in other table
    """
    def __str__(self):
        return self.title

    class Meta:
        app_label = 'matters'


class Matter(BaseModelMixin):
    case_id = models.CharField(max_length=50)

    # maybe type should be changed to category to conform to other tables
    # and to facilitate use of the codes table?
    type = models.ForeignKey(MatterType,
                             default=1,
                             on_delete=models.CASCADE,
                             related_name="types_matters")
    files_foldername = models.CharField(max_length=80,
                                        null=True,
                                        )
    date_opened = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
