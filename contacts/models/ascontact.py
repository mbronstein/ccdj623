from core.models import BaseModelMixin
from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class AsContact(BaseModelMixin):
    name = models.CharField(max_length=80,
                               blank=True,
                               null=True)
    address = models.CharField(max_length=80,
                               blank=True,
                               null=True)
    city = models.CharField(max_length=80,
                            blank=True,
                            null=True)
    state = models.CharField(max_length=80,
                             blank=True, null=True)
    country = models.CharField(max_length=80,
                               blank=True,
                               null=True)
    zipcode = models.CharField(max_length=80,
                           blank=True,
                           null=True)
    email = models.CharField(max_length=80,
                             blank=True,
                             null=True)
    phone = models.CharField(max_length=80,
                             blank=True,
                             null=True)

    class Meta:
        app_label = 'contacts'
        ordering = ['title']

        def __str__(self):
            return self.name
