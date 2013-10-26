from django.contrib.auth.models import AbstractUser
from django.db import models_

class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(_("age"))