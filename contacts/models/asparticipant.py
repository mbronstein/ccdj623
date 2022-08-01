from core.models import BaseModelMixin
from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class AsParticipant(BaseModelMixin):
    first_name = models.CharField(max_length=80,
                                  blank=True,
                                  null=True)

    middle_name = models.CharField(max_length=80,
                                   blank=True,
                                   null=True)

    last_name = models.CharField(max_length=80,
                                 blank=True,
                                 null=True)
    org_name = models.CharField(max_length=80,
                                blank=True,
                                null=True)
    address1 = models.CharField(max_length=80,
                                blank=True,
                                null=True)

    address2 = models.CharField(max_length=80,
                                blank=True,
                                null=True)
    city = models.CharField(max_length=80,
                            blank=True,
                            null=True)
    state = models.CharField(max_length=2,
                             blank=True, null=True,
                             default='MA')
    country = models.CharField(max_length=2,
                               blank=True,
                               null=True,
                               default='US')
    zipcode = models.CharField(max_length=30,
                               blank=True,
                               null=True)
    email = models.CharField(max_length=80,
                             blank=True,
                             null=True)

    phone1_area_code = models.CharField(max_length=80,
                                        blank=True,
                                        null=True)
    phone1 = models.CharField(max_length=80,
                              blank=True,
                              null=True)
    phone1_description = models.CharField(max_length=80,
                                          blank=True,
                                          null=True)

    phone2_area_code = models.CharField(max_length=80,
                                        blank=True,
                                        null=True)
    phone2 = models.CharField(max_length=80,
                              blank=True,
                              null=True)
    phone2_description = models.CharField(max_length=80,
                                          blank=True,
                                          null=True)

    phone3_area_code = models.CharField(max_length=80,
                                        blank=True,
                                        null=True)
    phone3 = models.CharField(max_length=80,
                              blank=True,
                              null=True)
    phone3_description = models.CharField(max_length=80,
                                          blank=True,
                                          null=True)
    phone4_area_code = models.CharField(max_length=80,
                                        blank=True,
                                        null=True,
                                        )
    phone4 = models.CharField(max_length=80,
                              blank=True,
                              null=True)
    phone4_description = models.CharField(max_length=80,
                                          blank=True,
                                          null=True)
    fax = models.CharField(max_length=80,
                           blank=True,
                           null=True)
    text_sms = models.CharField(max_length=80,
                                blank=True,
                                null=True)
    e_mail = models.CharField(max_length=80,
                              blank=True,
                              null=True)
    website = models.CharField(max_length=80,
                               blank=True,
                               null=True)
    tax_number = models.CharField(max_length=80,
                                  blank=True,
                                  null=True)
    date_of_birth = models.CharField(max_length=80,
                                     blank=True,
                                     null=True)
    display_name = models.CharField(max_length=80,
                                    blank=True,
                                    null=True)


class Meta:
    app_label = 'contacts'
    ordering = ['last_name', 'first_name', 'org_name']


def __str__(self):
    return f"{self.org},{self.last_name},{self.first_name}"
