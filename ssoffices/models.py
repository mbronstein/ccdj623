from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# from django.contrib.gis.db.models import PointField

# list of all ssa office downloaded from
# https://www.ssa.gov/open/data/FO-RS-Address-Open-Close-Time-App-Devs.html#dataDictionary
# on 11/29/20

USER_MODEL = get_user_model()

ROJurArray = None
OHOJurArray = None
DDSJurArray = None
PSCJurArray = None


def create_slug(city, state, type):
    return f"{city}-{state}-{type}".lower()


class SsOffice(models.Model):
    class Meta:
        app_label = "ssoffices"
        ordering = ["slug"]
        verbose_name = "SS Office"
        verbose_name_plural = "SSA Offices"

    class SsOfficeTypes(models.IntegerChoices):
        UNKNOWN = 1, "Unknown"
        FO = 2, "Field Office (FO)"
        DDS = 3, "Disability Determination Services (DDS)"
        HO = 4, "Office of Hearings Operations (OHO)"
        AC = 5, "Appeals Council (AC)"
        PC = 6, "Program Service Center (PSC)"
        PCMOD = 7, 'PC Mod (PC MOD'
        RO = 8, "Regional Office (RO)"
        NHC = 9, "National Hearing Center (NHC)"
        CSU = 10, "Central Scheduling Unit (CSU)"
        NCAC = 11, "National Case Assistance Center (NCAC"
        WSU = 12, "Workload Support Unit (WSU)"
        OTHER = 13, 'Other'

    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField(choices=SsOfficeTypes.choices,
                               default=1)
    slug = models.CharField(max_length=128,
                            null=True,
                            blank=True,
                            unique=True)
    display_name = models.CharField(max_length=128,
                                    null=True,
                                    blank=True)
    ssa_site_code = models.CharField(max_length=128, null=True, blank=True)
    ssa_office_name = models.CharField(max_length=128, null=True, blank=True)
    region = models.CharField(max_length=128, null=True, blank=True)
    ssa_last_updated = models.CharField(max_length=128, null=True, blank=True)
    # lookup_name = models.CharField(max_length=128)
    address1 = models.CharField(max_length=128, null=True, blank=True)
    address2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=128, null=True, blank=True)
    tel_public = PhoneNumberField(blank=True, null=True)
    tel_call_back = PhoneNumberField(blank=True, null=True)
    tel_admin = PhoneNumberField(blank=True, null=True)
    fax = PhoneNumberField(blank=True, null=True)
    # servicing_states = models.CharField(max_length=128, null=True, blank=True)
    # servicing_fos = models.CharField(max_length=128, null=True, blank=True)
    # servicing_zipcodes = models.CharField(max_length=128, null=True, blank=True)
    # servicing_ssns = models.CharField(max_length=128, null=True, blank=True)
    # geo_location = PointField(srid=4326, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='+',
                                 )

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='+',
                                    null=True,
                                    )

    def __str__(self):
        return self.slug

    # def get_absolute_url(self):
    #     return reverse('ssoffices:ssoffices', kwargs={'slug': self.slug})

    def as_dict(self):
        return self.__dict__

    @property
    def city_state_zip(self):
        return f"{self.city}, {self.state}  {self.zipcode}"

    @property
    def address_block(self):
        pass


class SsStaff(models.Model):
    class StaffTypes(models.TextChoices):
        ADM = ('ADM', "Asst District Manager, FO")
        ALJ = ('ALJ', "Administrative Law Judge, OHO")
        CR = ('CR', "Claims Representative, FO")
        DE = ('DE', "Disability Examiner, DDS")
        DM = ('DM', "District Manager, FO")
        GS = ('GS', "Group Supervisor, OHO")
        HA = ('HA', "Hearing Asst, OHO")
        HOD = ('HOD', "Hearing Office Director")
        HOS = ('HOS', "Office of Hearings Operations (OHO) Staff")
        OS = ('OS', "Operations Supervisor, FO")
        PCS = ('PCS', "Program Service Center Staff")
        SA = ('SA', "Staff Attorney, OHO")
        VDE = ('VDE', "Vocational Disability Examiner, DDS")
        CSU = ('CSU', "CSU Staff")

    class Meta:
        app_label = "ssoffices"
        verbose_name = "SSA Staff"
        verbose_name_plural = "SSA Staff"
        ordering = ['last_name', 'first_name', 'ssoffice']
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['ssoffice']),
            models.Index(fields=['type']),
        ]

    id = models.AutoField(primary_key=True)
    ssoffice = models.ForeignKey(SsOffice,
                                 on_delete=models.CASCADE,
                                 related_name='staff')
    type = models.CharField(choices=StaffTypes.choices,
                            max_length=128,
                            db_index=True,
                            blank=True, null=True)
    first_name = models.CharField(max_length=128,
                                  blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    salutation = models.CharField(max_length=128,
                                  blank=True, null=True)
    # honorific = models.CharField(max_length=128,
    #                              blank=True,
    #                              null=True, )
    tel = PhoneNumberField(blank=True, null=True)
    tel_ext = models.CharField(max_length=20,
                               blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # supervisor = models.ManyToManyField("SsStaff", blank=True)
    personal_fax = PhoneNumberField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now,
                                   null=True,
                                   blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='+',
                                   null=True,
                                   )
    modified_by = models.ForeignKey(USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='+',
                                    null=True,
                                    blank=True
                                    )


    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.type}, {self.ssoffice}"

    def __repr__(self):
        return f"{self.last_name}, {self.first_name}: {self.id} ({self.type})"

    def display_name(self):
        return f"{self.last_name}, {self.first_name}, {self.type}"
