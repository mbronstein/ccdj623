# tasks.models
# adapted from https://github.com/shacker/django-todo

import datetime
import os
import textwrap

from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import DEFAULT_DB_ALIAS, models
from django.db.transaction import Atomic, get_connection
from django.urls import reverse
from django.utils import timezone

from matters.models import Matter
from core.models.basemodelmixin import BaseModelMixin
from core import utils

USER_MODEL = get_user_model()


class TaskCategory(models.Model):
    class TaskTypeChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Unknown'
        CALL = 2, 'Call'
        WAIT = 3, 'Wait'
        EMAIL = 4, "Email"
        DRAFT = 5, 'Draft'
        REVIEW = 6, 'Review'
        UPLOAD = 7, "Send"
        OTHER = 8, 'Other'
        PAY = 9, 'Pay Bill'
        BILL = 10, 'Prepare Bill'
        RESEARCH = 11, "Research"
        FIX = 12, "Fix"
        SEND_FAX = 13, "Send Fax"

    id = models.BigAutoField
    type = models.IntegerField(choices=TaskTypeChoices.choices,
                               default=TaskTypeChoices.UNKNOWN)
    name = models.CharField(max_length=150,
                            unique=True)
    description = models.CharField(max_length=60,
                                   null=True,
                                   blank=True)
    notes = models.TextField(null=True,
                             blank=True)
    created_by = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
    )
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'tasks'
        verbose_name_plural = "task categories"


class Task(BaseModelMixin):
    category = models.ForeignKey('tasks.TaskCategory',
                                 # default=TaskCategory.objects.get(pk=1),
                                 null=True,
                                 on_delete=models.CASCADE,
                                 related_name="category_tasks")
    matter = models.ForeignKey('matters.Matter',
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='matter_tasks'
                               )

    due_date = models.DateField(blank=True,
                                null=True,
                                default=timezone.now,
                                )
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True,
                                      null=True
                                      )

    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name="user_task_assignments",
                                    on_delete=models.CASCADE
                                    )

    # for admin display
    @property
    def compact_due_date(self):
        return utils.compact_date(self.due_date, with_dow=False)

    @property
    def compact_dow_due_date(self):
        return utils.compact_date(self.due_date, with_dow=True)
    due_date.short_description = 'Due Date'

    class Meta:
        app_label = 'tasks'
        ordering = ['-due_date']

    def __str__(self):
        return f"{self.title}:{self.category}:{self.due_date} "

# # Has due date for an instance of this object passed?
# def overdue_status(self):
#     "Returns whether the Tasks's due date has passed or not."
#     if self.due_date and datetime.date.today() > self.due_date:
#         return True
#
# def __str__(self):
#     return self.title
#
# def get_absolute_url(self):
#     return reverse("task:task_detail", kwargs={"task_id": self.id})
#
# # Auto-set the Task creation / completed date
# def save(self, **kwargs):
#     # If Task is being marked complete, set the completed_date
#     if self.completed:
#         self.completed_date = datetime.datetime.now()
#     super(Task, self).save()
#
# def merge_into(self, merge_target):
#     if merge_target.pk == self.pk:
#         raise ValueError("can't merge a task with self")
#
#     # lock the comments to avoid concurrent additions of comments after the
#     # update request. these comments would be irremediably lost because of
#     # the cascade clause
#     with LockedAtomicTransaction(Comment):
#         Comment.objects.filter(task=self).update(task=merge_target)
#         self.delete()
#
# class Meta:
#     app_label = 'tasks'
#     ordering = ["priority", "created_date"]

#
# class Comment(models.Model):
#     """
#     Not using Django's built-in comments because we want to be able to save
#     a comment and change task details at the same time. Rolling our own since it's easy.
#     """
#
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
#         related_name="task_comments"
#     )
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=datetime.datetime.now)
#     email_from = models.CharField(max_length=320, blank=True, null=True)
#     email_message_id = models.CharField(max_length=255, blank=True, null=True)
#
#     body = models.TextField(blank=True)
#
#     class Meta:
#         # an email should only appear once per task
#         unique_together = ("task", "email_message_id")
#
#     @property
#     def author_text(self):
#         if self.author is not None:
#             return str(self.author)
#
#         assert self.email_message_id is not None
#         return str(self.email_from)
#
#     @property
#     def snippet(self):
#         body_snippet = textwrap.shorten(self.body, width=35, placeholder="...")
#         # Define here rather than in __str__ so we can use it in the admin list_display
#         return "{author} - {snippet}...".format(author=self.author_text, snippet=body_snippet)
#
#     def __str__(self):
#         return self.snippet
#
#
# class Attachment(models.Model):
#     """
#     Defines a generic file attachment for use in M2M relation with Task.
#     """
#
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(default=datetime.datetime.now)
#
#     #  file = models.FileField(upload_to=get_attachment_upload_dir, max_length=255)
#
#     def filename(self):
#         return os.path.basename(self.file.name)
#
#     def extension(self):
#         name, extension = os.path.splitext(self.file.name)
#         return extension
#
#     def __str__(self):
#         return f"{self.task.id} - {self.file.name}"
#
# #
# #
# # def get_attachment_upload_dir(instance, filename):
# #     """Determine upload dir for task attachment files.
# #     """
# #
# #     return "/".join(["tasks", "attachments", str(instance.task.id), filename])
# #
# #
# class LockedAtomicTransaction(Atomic):
#     """
#     modified from https://stackoverflow.com/a/41831049
#     this is needed for safely merging
#
#     Does a atomic transaction, but also locks the entire table for any transactions, for the duration of this
#     transaction. Although this is the only way to avoid concurrency issues in certain situations, it should be used with
#     caution, since it has impacts on performance, for obvious reasons...
#     """
#
#     def __init__(self, *models, using=None, savepoint=None):
#         if using is None:
#             using = DEFAULT_DB_ALIAS
#         super().__init__(using, savepoint)
#         self.models = models
#
#     def __enter__(self):
#         super(LockedAtomicTransaction, self).__enter__()
#
#         # Make sure not to lock, when sqlite is used, or you'll run into problems while running tests!!!
#         if settings.DATABASES[self.using]["ENGINE"] != "django.db.backends.sqlite3":
#             cursor = None
#             try:
#                 cursor = get_connection(self.using).cursor()
#                 for model in self.models:
#                     cursor.execute(
#                         "LOCK TABLE {table_name}".format(table_name=model._meta.db_table)
#                     )
#             finally:
#                 if cursor and not cursor.closed:
#                     cursor.close()

# class TaskList(models.Model):


#
#
#     name = models.CharField(max_length=60)
#     slug = models.SlugField(default="")
#     type = models.CharField(max_length=1, choices=TaskType.choices, blank=True)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
#     matter = models.ForeignKey(Matter, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ["name"]
#         verbose_name_plural = "Task Lists"
#
#         # Prevents (at the database level) creation of two lists with the same slug in the same group
#         unique_together = ("group", "slug")  # TODO: also need to make matter list unique as well
