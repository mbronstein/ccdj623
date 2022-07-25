from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from core.models import BaseModelMixin

USER_MODEL = get_user_model()


class Session(BaseModelMixin):
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.date} ({self.model} : {self.field_name}"

    total_time = models.DecimalField(decimal_places=1, null=True, blank=True)


    def calc_duration(self):
        d = (self.end_time - self.start_time)

    class Meta:
        app_label = 'timekeeping'


