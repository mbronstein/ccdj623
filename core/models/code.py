from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from core.models import BaseModelMixin

USER_MODEL = get_user_model()


class Code(BaseModelMixin):
    class ModelChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Unknown'
        EVENT = 2, 'Event'
        MATTER = 3, 'Matter'
        TASK = 4, 'Task'
        CASEENTRY = 5, 'Case Entry'

    model = models.IntegerField(choices=ModelChoices.choices, default=1)
    field_name = models.CharField(max_length=30,
                                  blank=True,
                                  null=True)

    def __str__(self):
        return f"{self.title} ({self.model} : {self.field_name}"

    class Meta:
        app_label = 'core'
