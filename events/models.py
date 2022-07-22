from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import DEFAULT_DB_ALIAS, models
from django.db.transaction import Atomic, get_connection
from django.urls import reverse
from django.utils import timezone
from django_ical.views import ICalFeed

USER_MODEL = get_user_model()


class EventCategory(models.Model):
    class EventTypeChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Unknown'
        CALL = 2, 'Call'
        CONF = 3, 'Conference'
        DEADLINE = 4, "Deadline"
        VIDEO = 5, 'Video Conf'
        HEARING = 6, 'Hearing'
        MEET = 7, "Meeting"
        PRESENTATION = 8, "Presentation"
        OTHER = 9, 'Other'
        WARNING = 10, 'Deadline Warning'

    name = models.CharField(max_length=150)
    type = models.IntegerField(choices=EventTypeChoices.choices,
                               default=EventTypeChoices.UNKNOWN)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_event_categories"
    )
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'events'
        verbose_name_plural = "event categories"


class Event(models.Model):
    class EventStatusType(models.IntegerChoices):
        UNKNOWN = 1, "Unknown"
        PENDING = 2, "Pending"
        CANCELLED = 3, 'Cancelled'
        DONE = 4, 'Done'
        ONHOLD = 5, 'On Hold'
        OTHER = 6, 'Other'

    # class LocationChoices(models.TextChoices):
    #     UNKNOWN = "unk", "Unknown"
    #     OTHER = "other", "Other"
    #     OFFICE = "office", "Office"
    #     CALL = "call", "Call"
    #
    title = models.CharField(max_length=140)
    category = models.ForeignKey('EventCategory',
                                 null=True,
                                 on_delete=models.CASCADE,
                                 related_name="event_event_categories",
                                 )
    matter = models.ForeignKey('matters.Matter',
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='event_matters',

                               )
    start_datetime = models.DateTimeField(null=True)
    length = models.IntegerField(default=30)
    # EndDateTime = models.DateTimeField(null=True)
    attendees = models.CharField(max_length=60, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    status = models.IntegerField(choices=EventStatusType.choices, default=EventStatusType.PENDING)
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

    # for admin display
    def compact_start_datetime(self):
        return self.start_datetime.strftime("%m/%d/%y %I:%M %p (%a)")

    compact_start_datetime.short_description = 'Date/Time'

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                if field.verbose_name != 'event'
                else
                (field.verbose_name,
                 Event.objects.get(pk=field.value_from_object(self)).name)
                for field in self.__class__._meta.fields[1:]
                ]

    class Meta:
        app_label = 'events'
        ordering = ["priority", "created_date"]


class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//cms.bronsteinlaw.com//Example//EN'
    timezone = 'UTC'
    file_name = "event.ics"

    def items(self):
        return Event.objects.all().order_by('-start_datetime')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return item.start_datetime
