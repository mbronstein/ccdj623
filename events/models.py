from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import DEFAULT_DB_ALIAS, models
from django.db.transaction import Atomic, get_connection
from django.urls import reverse
from django.utils import timezone

import matters.models
from matters.models import Matter

USER_MODEL = get_user_model()


class EventType(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_eventtypes"
    )
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'events'


class Event(models.Model):
    # class EventType(models.TextChoices):
    #     CALL = 'CALL', 'Call'
    #     CONF = 'CONF', 'Conference'
    #     DEADLINE = 'DEAD', "Deadline"
    #     VIDEO = 'VID', 'Video Conf'
    #     SS_HEARING = 'OHO_HEAR', 'OHO Hearing'
    #     MEET = 'MEET', "Meeting"
    #     PRESENTATION = 'PRES', "Presentation"
    #     OTHER = 'OTHER', 'Other'
    #     WARNING = 'WARN', 'Deadline Warning'

    # class StatusType(models.TextChoices):
    #     SCHEDULED = 'SCHED', 'Scheduled'
    #     CANCELLED = 'CANC', 'Cancelled'
    #     DONE = 'DONE', 'Done'
    #     ONHOLD = 'ONHOLD', 'On Hold'
    #     OTHER = 'OTHER', 'Other'

    # class LocationChoices(models.TextChoices):
    #     UNKNOWN = "unk", "Unknown"
    #     OTHER = "other", "Other"
    #     OFFICE = "office", "Office"
    #     CALL = "call", "Call"
    #

    title = models.CharField(max_length=140)
    type = models.ForeignKey('EventType',
                             null=True,
                             on_delete=models.CASCADE,
                             related_name="event_eventtypes",
                             )
    matter = models.ForeignKey('matters.Matter',
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='event_matters',

                               )
    startdatetime = models.DateTimeField(null=True)
    length = models.IntegerField(default=30)
    # EndDateTime = models.DateTimeField(null=True)
    attendees = models.CharField(max_length=60, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    # status = models.ForeignKey("EventType", default='StatusType.OTHER',related_name="event_types")
    created_date = models.DateField(default=timezone.now,
                                    )

    created_by = models.ForeignKey(USER_MODEL,
                                   null=True,
                                   related_name="event_created_by",
                                   on_delete=models.CASCADE
                                   )

    assigned_to = models.ForeignKey(USER_MODEL,
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
        app_label = 'events'
        ordering = ["priority", "created_date"]
