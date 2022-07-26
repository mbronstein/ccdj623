# ccdj623/entries/models/models.py
#
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


class EntryCategory(BaseModelMixin):
    class EntryTypeChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Unknown'
        NOTE = 2, 'Note'
        CALL = 3, 'Call'
        EMAIL = 4, 'Email'
        SMS = 5, 'SMS'
        DOC = 6, "Document"
        OTHER = 7, "Other"
        VOICEMAIL = 8, 'Voicemail'
        DICTATION = 9, 'Dictation'
        FORM = 10, 'Form'

    type = models.IntegerField(choices=EntryTypeChoices.choices,
                               default=EntryTypeChoices.UNKNOWN)

    class Meta:
        app_label = 'entries'
        verbose_name_plural = "entry categories"

    def __str__(self):
        return f"{self.title}({self.type}"


class CaseEntry(BaseModelMixin):
    category = models.ForeignKey('entries.EntryCategory',
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE,
                                 related_name='categories'
                                 )
    matter = models.ForeignKey("matters.Matter",
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='matters',
                               )

    # file = models.FileField(upload_to=filefolder_name,
    #                         null=True,
    #                         blank=True)

    time_spent = models.DecimalField(default=0,
                                     decimal_places=1,
                                     max_digits=3,
                                     )

    class Meta:
        app_label = 'entries'
        verbose_name = 'case entry'
        verbose_name_plural = 'case entries'

    def __str__(self):
        return f"{self.title}"

    # for admin display
    def compact_datetime(self):
        return self.datetime.strftime("%m/%d/%y %I:%M %p (%a)")

    compact_datetime.short_description = 'Date/Time'
    #
    # def file_folder_name(instance, filename):
    #     return instance.matter.title

    # def save(self, *args, **kwargs):
    #     self.modified = timezone.now()
    #     super().save(*args, **kwargs)

    # # objects = InheritanceManager()

    # status = models.CharField(max_length=20,
    #                           choices=EntryStatusChoices.choices,
    #                           default="NEW"
    #                           )
    # originator_type = models.CharField(max_length=20, choices=Entry)
    # recipient_type = models.CharField(max_length=20, choices=CategoryChoices)
    # originator = models.CharField(max_length=80, default="unk")
    # recipient = models.CharField(max_length=80, default="unk")
    # new = models.BooleanField(default=True)
    # io_direction = models.CharField(max_length=20,
    #                                 choices=EntryIoChoices.choices,
    #                                 default="UNK")
    #
    # entry_source = models.CharField(max_length=20,
    #                                 choices=EntrySourceChoices.choices,
    #                                 default="UNK")
    #
    # received = models.DateField(blank=True)  # when received by LOMB
    #
    # billed_time = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    # billing_label = models.CharField(max_length=80, null=True, blank=True)

    # user = models.ForeignKey(USER_MODEL,
    #                          on_delete=models.CASCADE,
    #                          related_name='%(class)s_users'
    #                          )
    # deleted = models.BooleanField(default=True)
    # created_by = models.ForeignKey(USER_MODEL,
    #                                on_delete=models.CASCADE,
    #                                related_name='%(class)s_notes_created',
    #                                default=2
    #                                )
    # modified = models.DateTimeField(auto_now_add=True)
    #
    # def __str__(self):
    #     return self.title + "(Entry)"
    #
    # class Meta:
    #     app_label = 'case_entries'
    #     verbose_name_plural = 'entries'
    #
    # objects = InheritanceManager()
    #
    # # startdate = models.DateTimeField(default=timezone.now)
    # # enddate = models.DateTimeField(default=timezone.now)
    # # duration = models.DecimalField(default=0, max_digits=5, decimal_places=2)

# class EntryIoChoices(models.TextChoices):
#     OTHER = "OTH", "Other"
#     IN = 'IN', "Incoming"
#     OUT = 'OUT', "Outgoing"
#     UNKNOWN = "UNK", 'Unknown'
#
# class EntryStatusChoices(models.TextChoices):
#     NEW = "N", "New"
#     UNKNOWN = "U", "Unknown"
#     DRAFT = "D", "Draft"
#     SENT = "S", "Sent"
#     PROCESSED = "P", "Processed"
#
# class EntrySourceChoices(models.TextChoices):
#     UNKNOWN = "UNK", "Unknown"
#     DELIVERED = "DELIVERED", "Received by Mail or Delivery"
#     EMAIL = 'EMAIL', 'Email'
#     SMS = 'SMS', 'SMS'
#     FAX = 'FAX", "Fax"'
#     PHONE = "CALL", "Phone call"
#     OTHER = "OTH", "Other"

#  class Sender    ("other", "Other"),
#     ("unk", "unknown"),
#     ('na', "Not applicable"),
#     ("client", "Client"),
#     ("ssfo", "SSA FO"),
#     ("dds", "DDS"),
#     ("oho", "OHO"),
#     ("alj", "ALJ"),
#     ("ac", "Appeals Council"),
#     ("psc", "Program Service Center"),
#     ("med", "Medical Provider"),
#     ("insco", "Ins Co"),
# )
#
#
# class EmailEntry(CaseEntry):
#     # Inherited Choice objects:
#     #   status, category, subcategory, io, inputsource
#
#     Message = models.ForeignKey(EmailMessage, on_delete=models.CASCADE, null=True)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         type = "email"
#
#     class CategoryChoices(models.TextChoices):
#         GENERAL = "general", "General"
#
#     class Meta:
#         verbose_name_plural = "email_entries"
#
#     # class StatusChoices(models.TextChoices):
#     #     NEW = "new", "New"
#     #     READ = "read", "Read"
#     #     DRAFT = "draft", "Draft"
#     #     FINAL = "final", "Final"
#     #     UNKNOWN = "unk", "Unknown"
#
#     # DEFAULT_STATUS = StatusChoices.NEW
#
#
# class SmsEntry(CaseEntry):
#     # Inherited Choice objects:
#     #  subcategory, io, inputsource, originatortype, recipienttype
#
#     class CategoryChoices(models.TextChoices):
#         WITH_CLIENT = "client", "Client"
#         WITH_OTHER = "other", "Other"
#         UNKNOWN = "unk", "Unknown"
#
#     class StatusChoices(models.TextChoices):
#         NEW = "new", "New"
#         READ = "read", "Read"
#         DRAFT = "draft", "Draft"
#         FINAL = "final", "Final"
#         UNKNOWN = "unk", "Unknown"
#
#     class Meta:
#         verbose_name_plural = "doc_entries"
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.rec_type = "sms"
#
#
# class DocEntry(CaseEntry):
#     # Inherited Choice objects:
#     #   status, category, subcategory, io, inputsource, originatortype, recipienttype
#
#     class Meta:
#         verbose_name_plural = "doc_entries"
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.rec_type = "doc"
#         self.file = models.FileField(upload_to="X")
#         self.CategoryChoices = (
#
#         )
#         self.SubcategoryChoices = ()
#         self.StatusChoices = ()
#
#     file = models.FileField()
#
#     # class DocCategoryChoices(models.TextChoices):
#     #     UNKNOWN = "unk", "Unknown"
#     #     LETTER = "letter", "Letter"
#     #     FORM = "form", "Form"
#     #     RECORD = "record", "Record"
#     #     SSA_FORM = "ssa_form", "SSA Form"
#     #     SSA_LETTER = "ssa_letter", "SSA Letter"
#     #     OHO_NOTICE = "oho_notice", "OHO Notice"
#     #     INS_LETTER = "ins_letter", "INS Letter"
#     #     INS_FORM = "ins_form", "INS Form"
#     #     MED_RECORD = "med_rec", "Medical Records"
#     #     OTHER = "other", "Other"
#     #
#     # class DocStatusChoices(models.TextChoices):
#     #     NEW = "new", "New"
#     #     READ = "read", "Read"
#     #     DRAFT = "draft", "Draft"
#     #     FINAL = "final", "Final"
#     #     SENT = "sent", "Sent"
#     #     UNKNOWN = "unk", "Unknown"
#
#
# class EventEntry(CaseEntry):
#     # Inherited Choice objects:
#     #   status, category, subcategory, io, inputsource, originatortype, recipienttype
#     class Meta:
#         verbose_name_plural = "event_entries"
#     #
#     # class CategoryChoices(models.TextChoices):
#     #     CLIENT_MEETING = "cl_meeting", "Client Meeting"
#     #     MEETING = "meeting", "Meeting"
#     #     CALL = "call", "Call"
#     #     SS_HEARING = "sshearing", "SS Hearing"
#     #     PRES = "pres", "Presentation"
#     #     OTHER = "other", "Other"
#     #     UNKNOWN = "unk", "Unknown"
#     #     WARNING = "warning", "Warning"
#     #     DEADLINE = "dead", "Deadline"
#     #     REMINDER = "reminder", "Reminder"
#     #
#     # class StatusChoices(models.TextChoices):
#     #     UNKNOWN = "unk", "Unknown"
#     #     SCHEDULED = "sched" "Scheduled"
#     #     CANCELLED = "cancelled", "Cancelled"
#     #     COMPLETED = "completed", "Completed"
#     #     ON_HOLD = "on_hold", "On Hold"
#     #     OTHER = "other", "Other"
#     #
#     # class LocationChoices(models.TextChoices):
#     #     UNKNOWN = "unk", "Unknown"
#     #     OTHER = "other", "Other"
#     #     OFFICE = "office", "Office"
#     #     CALL = "call", "Call"
#     #
#
#
# class NoteEntry(CaseEntry):
#     class Meta:
#         verbose_name_plural = "note_entries"
#
#     # class CategoryChoices(models.TextChoices):
#     #     CASE_STATUS = "status", "Status"
#     #     RESEARCH = "research", "Research"
#     #     REVIEW = "review", "Review"
#     #     EVENT_NOTES = "event-notes", "Event Notes"
#     #     OTHER = "other", "Other"
#     #     UNKNOWN = "unk", "Unknown"
#     #
#     # class StatusChoices(models.TextChoices):
#     #     NEW = "new", "New"
#     #     UNKNOWN = "unk", "Unknown"
#     #     OTHER = "other", "Other"
#
#
# class CaseReviewEntry(CaseEntry):
#     class Meta:
#         verbose_name_plural = "case_review_entries"
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#
# class TaskEntry(CaseEntry):
#     owner = models.ForeignKey(User,
#                               on_delete=models.CASCADE,
#                               related_name='owners')
#     assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignees')
#
#     class Meta:
#         verbose_name_plural = "task_entries"
#     #
#     # class TaskStatusChoices(models.TextChoices):
#     #     NEW = "new", "New"
#     #     ASSIGNED = "assigned", "Assigned"
#     #     PENDING = "pending", "Pending"
#     #     UNKNOWN = "unk", "Unknown"
#     #     WAIT_RESPONSE = "wait_resp", "Waiting for Response"
#     #
#     # class TaskCategoryChoices(models.TextChoices):
#     #     CALL = "call", "Call"
#     #     EMAIL = "email", "Email"
#     #     LETTER = "letter", "Letter"
#     #     FORM = "form", "Form"
#     #     OTHER = "other",
#     #     UNKNOWN = "unk", "Unknown"
#     #     RESEARCH = "research", "Research"
#     #     ABSTRACT = "abstract", "Abstract"  # shoald this be Digest?
#     #     DRAFTING = "drafting", "Drafting"
