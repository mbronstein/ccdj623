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


