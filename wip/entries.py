# ccdj623/matters/models/entries.py
from django.db.models import Choices
from django.utils import timezone
# from django_mailbox.models import Message as EmailMessage
# from wip.matters.models import BaseMatter, Choices
from django.db import models
from django.contrib.auth.models import User
import uuid
from taggit.managers import TaggableManager
from phonenumber_field.modelfields import PhoneNumberField


class BaseEntry(models.Model):

    class CategoryChoices(models.TextChoices):
        NONE = 'FR', _('Freshman')
        UNKNOWN = 'UNK', 'Unknown')
    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }
    DefCategoryChoices = (
        ("none", "None"),
        ("unk", "Unknown"),
    )
    CategoryChoices = DefCategoryChoices

    DefSubcategoryChoices = Choices(
        ("none", "None"),
        ("na", "Not Applicable")
    )
    SubcategoryChoices = DefSubcategoryChoices

    DefStatusChoices = Choices(
        ("new", "New"),
        ("none", "None"),
        ("unk", "Unknown"),
        ('prospect', 'Prospect'),
        ('rtc', 'Ready to Close'),
        ('closed', 'Closed'),
        ('archived', 'Archived'),
    )
    StatusChoices = DefStatusChoices


    DefIoChoices = Choices(
        ("in", "In"),
        ("out", "Out"),
        ("unk", "Unknown"),
        ("na", "Not Applicable")

    )

    IoChoices=DefIoChoices

    DefInputSourceChoices = Choices(
        ("mail", "Mail"),
        ("email", "Email"),
        ('fax', "Fax"),
        ('sms', "SMS"),
        ('phone', "Phone"),
        ("hand", "Hand"),
        ("other", "Other"),
         ("unk", "unknown")
    )

    InputSourceChoices = DefInputSourceChoices

    DefOriginatorTypeChoices = (
        ("other", "Other"),
        ("unk", "unknown"),
        ('na', "Not applicable"),
        ("client", "Client"),
        ("ssfo", "SSA FO"),
        ("dds", "DDS"),
        ("oho", "OHO"),
        ("alj", "ALJ"),
        ("ac", "Appeals Council"),
        ("psc", "Program Service Center"),
        ("med", "Medical Provider"),
        ("insco", "Ins Co"),
    )

    OriginatorTypeChoices =DefOriginatorTypeChoices

    DefRecipientTypeChoices = DefOriginatorTypeChoices

    RecipientTypeChoices = DefRecipientTypeChoices

    rectype = "entry"

    class Meta:
        # verbose_name_plural = "entries"
        abstract=True
    rec_type=None
    uuid = models.UUIDField(primary_key=False,
                            default=uuid.uuid4,
                            editable=False)
    category = models.CharField(max_length=20,
                                choices=CategoryChoices,
                                default="unk"
                                )
    subcategory = models.CharField(max_length=20,
                                   choices=SubcategoryChoices,
                                   default="unk",
                                   )
    status = models.CharField(max_length=20,
                              choices=StatusChoices,
                              default="new"
                              )
    matter = models.ForeignKey(BaseMatter,
                               on_delete=models.CASCADE)
    tags = TaggableManager()
    status_detail = models.CharField(max_length=80, default="")

    startdate=models.DateTimeField(default=timezone.now)
    enddate = models.DateTimeField(default=timezone.now)
    duration = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    description = models.CharField(max_length=100,
                                   blank=True)  # aka subject in email object
    memo = models.TextField(blank=True)
    originator_type = models.CharField(max_length=20)
    recipient_type = models.CharField(max_length=20, choices=CategoryChoices)
    originator = models.CharField(max_length=80, default="unk")
    recipient = models.CharField(max_length=80, default="unk")
    new = models.BooleanField(default=True)
    io_direction = models.CharField(max_length=20,
                                    choices=IoChoices,
                                    default="unk")

    input_source = models.CharField(max_length=20,
                                    choices=InputSourceChoices,
                                    default="unk")

    received = models.DateField(blank=True)  # when received by LOMB

    last_review = models.DateField(max_length=30, blank=True)
    review_interval = models.PositiveSmallIntegerField(default=30)
    billed_time = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    billing_label = models.CharField(max_length=80, default=rectype)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=True)
    entered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}:{1}".format(self.rectype, self.startdate)


class CallEntry(BaseEntry):
    #Inherited Choice objects:
    #   status, category, subcategory, io, inputsource, originatortype, recipienttype

    phonenumber = PhoneNumberField()
    cid_info = models.CharField(max_length=30, blank=True)
    voice_file = models.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rec_type = "call"

    class Meta:
        verbose_name_plural = "call_entries"


class EmailEntry(BaseEntry):
    # Inherited Choice objects:
    #   status, category, subcategory, io, inputsource

    Message = models.ForeignKey(EmailMessage, on_delete=models.CASCADE, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rec_type  = "email"


    class CategoryChoices(models.TextChoices):
        GENERAL = "general", "General"



    class Meta:
        verbose_name_plural = "email_entries"

    # class StatusChoices(models.TextChoices):
    #     NEW = "new", "New"
    #     READ = "read", "Read"
    #     DRAFT = "draft", "Draft"
    #     FINAL = "final", "Final"
    #     UNKNOWN = "unk", "Unknown"

    # DEFAULT_STATUS = StatusChoices.NEW

class SmsEntry(BaseEntry):
    # Inherited Choice objects:
    #  subcategory, io, inputsource, originatortype, recipienttype


    class CategoryChoices(models.TextChoices):
        WITH_CLIENT = "client", "Client"
        WITH_OTHER = "other", "Other"
        UNKNOWN = "unk", "Unknown"

    class StatusChoices(models.TextChoices):
        NEW = "new", "New"
        READ = "read", "Read"
        DRAFT = "draft", "Draft"
        FINAL = "final", "Final"
        UNKNOWN = "unk", "Unknown"

    class Meta:
        verbose_name_plural = "doc_entries"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rec_type = "sms"

class DocEntry(BaseEntry):
    # Inherited Choice objects:
    #   status, category, subcategory, io, inputsource, originatortype, recipienttype

    class Meta:
        verbose_name_plural = "doc_entries"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rec_type = "doc"
        self.file = models.FileField(upload_to="X") #TODO fix this so stored correctly in subdir with matter name.
        self.CategoryChoices= (

        )
        self.SubcategoryChoices = ()
        self.StatusChoices = ()

    file = models.FileField()


    # class DocCategoryChoices(models.TextChoices):
    #     UNKNOWN = "unk", "Unknown"
    #     LETTER = "letter", "Letter"
    #     FORM = "form", "Form"
    #     RECORD = "record", "Record"
    #     SSA_FORM = "ssa_form", "SSA Form"
    #     SSA_LETTER = "ssa_letter", "SSA Letter"
    #     OHO_NOTICE = "oho_notice", "OHO Notice"
    #     INS_LETTER = "ins_letter", "INS Letter"
    #     INS_FORM = "ins_form", "INS Form"
    #     MED_RECORD = "med_rec", "Medical Records"
    #     OTHER = "other", "Other"
    #
    # class DocStatusChoices(models.TextChoices):
    #     NEW = "new", "New"
    #     READ = "read", "Read"
    #     DRAFT = "draft", "Draft"
    #     FINAL = "final", "Final"
    #     SENT = "sent", "Sent"
    #     UNKNOWN = "unk", "Unknown"



class EventEntry(BaseEntry):
    # Inherited Choice objects:
    #   status, category, subcategory, io, inputsource, originatortype, recipienttype
    class Meta:
        verbose_name_plural = "event_entries"
    #
    # class CategoryChoices(models.TextChoices):
    #     CLIENT_MEETING = "cl_meeting", "Client Meeting"
    #     MEETING = "meeting", "Meeting"
    #     CALL = "call", "Call"
    #     SS_HEARING = "sshearing", "SS Hearing"
    #     PRES = "pres", "Presentation"
    #     OTHER = "other", "Other"
    #     UNKNOWN = "unk", "Unknown"
    #     WARNING = "warning", "Warning"
    #     DEADLINE = "dead", "Deadline"
    #     REMINDER = "reminder", "Reminder"
    #
    # class StatusChoices(models.TextChoices):
    #     UNKNOWN = "unk", "Unknown"
    #     SCHEDULED = "sched" "Scheduled"
    #     CANCELLED = "cancelled", "Cancelled"
    #     COMPLETED = "completed", "Completed"
    #     ON_HOLD = "on_hold", "On Hold"
    #     OTHER = "other", "Other"
    #
    # class LocationChoices(models.TextChoices):
    #     UNKNOWN = "unk", "Unknown"
    #     OTHER = "other", "Other"
    #     OFFICE = "office", "Office"
    #     CALL = "call", "Call"
    #

class NoteEntry(BaseEntry):
    class Meta:
        verbose_name_plural = "note_entries"

    # class CategoryChoices(models.TextChoices):
    #     CASE_STATUS = "status", "Status"
    #     RESEARCH = "research", "Research"
    #     REVIEW = "review", "Review"
    #     EVENT_NOTES = "event-notes", "Event Notes"
    #     OTHER = "other", "Other"
    #     UNKNOWN = "unk", "Unknown"
    #
    # class StatusChoices(models.TextChoices):
    #     NEW = "new", "New"
    #     UNKNOWN = "unk", "Unknown"
    #     OTHER = "other", "Other"

class CaseReviewEntry(BaseEntry):
    class Meta:
        verbose_name_plural = "case_review_entries"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TaskEntry(BaseEntry):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='owners')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignees')

    class Meta:
        verbose_name_plural = "task_entries"
    #
    # class TaskStatusChoices(models.TextChoices):
    #     NEW = "new", "New"
    #     ASSIGNED = "assigned", "Assigned"
    #     PENDING = "pending", "Pending"
    #     UNKNOWN = "unk", "Unknown"
    #     WAIT_RESPONSE = "wait_resp", "Waiting for Response"
    #
    # class TaskCategoryChoices(models.TextChoices):
    #     CALL = "call", "Call"
    #     EMAIL = "email", "Email"
    #     LETTER = "letter", "Letter"
    #     FORM = "form", "Form"
    #     OTHER = "other",
    #     UNKNOWN = "unk", "Unknown"
    #     RESEARCH = "research", "Research"
    #     ABSTRACT = "abstract", "Abstract"  # shoald this be Digest?
    #     DRAFTING = "drafting", "Drafting"
