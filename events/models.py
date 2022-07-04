from django.db import models
import datetime
import os
import textwrap

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import DEFAULT_DB_ALIAS, models
from django.db.transaction import Atomic, get_connection
from django.urls import reverse
from django.utils import timezone

from matters.models import Matter


class Event(models.Model):

    class EventType(models.TextChoices):
        CALL = 'CALL', 'Call'
        CONF = 'CONF', 'Conference'
        DEADLINE = 'DEAD', "Deadline"
        VIDEO = 'VID', 'Video Conf'
        SS_HEARING = 'OHO_HEAR', 'OHO Hearing'
        MEET = 'MEET', "Meeting"
        PRESENTATION = 'PRES', "Presentation"
        OTHER = 'OTHER', 'Other'
        WARNING= 'WARN', 'Deadline Warning'

    class StatusType(models.TextChoices):
        SCHEDULED = 'SCHED', 'Scheduled'
        CANCELLED = 'CANC', 'Cancelled'
        DONE = 'DONE', 'Done'
        ONHOLD = 'ONHOLD', 'On Hold'
        OTHER = 'OTHER', 'Other'


        # class LocationChoices(models.TextChoices):
        #     UNKNOWN = "unk", "Unknown"
        #     OTHER = "other", "Other"
        #     OFFICE = "office", "Office"
        #     CALL = "call", "Call"
        #

    title = models.CharField(max_length=140)
    type = models.CharField(max_length=10, choices=EventType.choices, default=EventType.OTHER)
    matter = models.ForeignKey(Matter,
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='event_matter'
                               )
    startdatetime = models.DateTimeField(null=True)
    length = models.IntegerField(default=30)
    # EndDateTime = models.DateTimeField(null=True)
    attendees = models.CharField(max_length=60, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=10, choices=StatusType.choices, default='StatusType.OTHER')
    created_date = models.DateField(default=timezone.now,
                                    )

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="event_created_by",
                                   default=1,
                                   on_delete=models.CASCADE,
                                   )
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    default=1,
                                    related_name="event_assigned_to",
                                    on_delete=models.CASCADE,
                                    )
    note = models.TextField(blank=True,
                            null=True
                            )
    priority = models.PositiveIntegerField(default=0
                                           )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"event_id": self.id})

    class Meta:
        ordering = ["priority", "created_date"]
