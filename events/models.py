from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import DEFAULT_DB_ALIAS, models
from django.db.transaction import Atomic, get_connection
from django.urls import reverse
from django.utils import timezone
from django_ical.views import ICalFeed
from core.models import BaseModelMixin

USER_MODEL = get_user_model()


class EventCategory(BaseModelMixin):
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

    type = models.IntegerField(choices=EventTypeChoices.choices,
                               default=EventTypeChoices.UNKNOWN)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        app_label = 'events'
        verbose_name_plural = "event categories"


class Event(BaseModelMixin):
    class EventStatusType(models.IntegerChoices):
        UNKNOWN = 1, "Unknown"
        PENDING = 2, "Pending"
        CANCELLED = 3, 'Cancelled'
        DONE = 4, 'Done'
        ONHOLD = 5, 'On Hold'
        OTHER = 6, 'Other'
        SCHEDULED = 7, 'Scheduled'
        WAIT_RESCHEDULE = 8, "Wait to be rescheduled"

    # class LocationChoices(models.TextChoices):
    #     UNKNOWN = "unk", "Unknown"
    #     OTHER = "other", "Other"
    #     OFFICE = "office", "Office"
    #     CALL = "call", "Call"
    #

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
    length = models.IntegerField(default=30)
    # EndDateTime = models.DateTimeField(null=True)
    attendees = models.CharField(max_length=80, null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    location_url = models.URLField(null=True, blank=True)
    status = models.IntegerField(choices=EventStatusType.choices, default=EventStatusType.PENDING)

    assigned_to = models.ForeignKey(USER_MODEL,
                                    default=1,
                                    related_name="event_assigned_to",
                                    on_delete=models.CASCADE,
                                    )

    priority = models.PositiveIntegerField(default=0
                                           )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"event_id": self.id})

    # for admin display
    def compact_datetime(self):
        return self.datetime.strftime("%m/%d/%y %I:%M %p (%a)")

    compact_datetime.short_description = 'Date/Time'

    # def get_fields(self):
    #     return [(field.verbose_name, field.value_from_object(self))
    #             if field.verbose_name != 'event'
    #             else
    #             (field.verbose_name,
    #              Event.objects.get(pk=field.value_from_object(self)).name)
    #             for field in self.__class__._meta.fields[1:]
    #             ]

    class Meta:
        app_label = 'events'



class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//cms.bronsteinlaw.com//Example//EN'
    timezone = 'UTC'
    file_name = "event.ics"
    #
    # def items(self):
    #     return Event.objects.all().order_by('-start_datetime')
    #
    # def item_title(self, item):
    #     return item.title
    #
    # def item_description(self, item):
    #     return item.description
    #
    # def item_start_datetime(self, item):
    #     return item.start_datetime
