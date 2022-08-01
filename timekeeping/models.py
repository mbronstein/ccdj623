from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from core.models import BaseModelMixin

USER_MODEL = get_user_model()


class WorkSession(BaseModelMixin):
    user = models.ForeignKey(USER_MODEL,
                             related_name='worksession_users',
                             on_delete=models.CASCADE
                             )
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.datetime} ({self.start_time} : {self.end_time} ({self.duration})"

    def calc_duration(self):
        d = (self.end_time - self.start_time)

    class Meta:
        app_label = 'timekeeping'
        ordering = ['datetime']


