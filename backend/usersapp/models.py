from uuid import uuid4


from django.contrib.auth.models import AbstractUser
from django.db import models


class MainUser(AbstractUser):
    id              = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username        = models.CharField(max_length=64, unique=True)
    email           = models.EmailField(max_length=256, blank=False, unique=True)
    first_name      = None
    last_name       = None

