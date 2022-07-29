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


class DraftEmail(BaseModelMixin):
    matter = models.ForeignKey(Matter,
                               on_delete=models.CASCADE,
                               related_name="matters_email1"
                               )
    subject = models.CharField(max_length=80,
                               null=True,
                               blank=True
                               )
    MessageID = models.CharField(max_length=30,
                                 null=True,
                                 blank=True)
    from_name = models.CharField(max_length=30,
                                 null=True,
                                 blank=True)

    from_email = models.CharField(max_length=30,
                                  null=True,
                                  blank=True)

    to_emails = models.JSONField()

    cc_emails = models.JSONField(max_length=120,
                                 null=True,
                                 blank=True)
    bcc_emails = models.JSONField(max_length=120,
                                  null=True,
                                  blank=True)
    html_body = models.(null=True,
                                 blank=True
                                 )
    text_body = models.TextField(null=True,
                                 blank=True
                                 )

    # attachment1 = # attachments = ?

    class Meta:
        app_label = 'emailclient'

    def __str__(self):
        return f"{self.subject}: {self.matter.title}"
